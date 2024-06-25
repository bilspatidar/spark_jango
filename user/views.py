from django.core.mail import send_mail
from django.contrib.auth import authenticate
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from .models import CustomUser
from .serializers import UserSerializer, UserLoginSerializer
from rest_framework.permissions import IsAuthenticated
from .serializers import PasswordChangeSerializer, ForgotPasswordSerializer, PasswordResetSerializer
from django.contrib.auth import get_user_model
from django.conf import settings
import random
import string
from django.utils import timezone
from utils.common_helpers import generate_token, token_expire_time
from rest_framework.permissions import AllowAny
from rest_framework.generics import UpdateAPIView
from django.core.cache import cache



User = get_user_model()

class UserRegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response({
                "status": "Success",
                "data": serializer.data,
                "errors": ""
            }, status=status.HTTP_201_CREATED, headers=headers)
        else:
            return Response({
                "status": "Failed",
                "data": "",
                "errors": serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)

class UserLoginView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']
        password = serializer.validated_data['password']
        
        # First check if the user exists
        try:
            user = CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            return Response({'status': 'Failed', 'error': 'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Check if the user is active
        if not user.is_active:
            return Response({'status': 'Failed', 'error': 'Account is not activated'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Authenticate the user
        user = authenticate(email=email, password=password)
        if user:
            user_serializer = UserSerializer(user)
            refresh = RefreshToken.for_user(user)
            return Response({
                'status': 'Success',
                'user_details': user_serializer.data,
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        
        # If authentication fails
        return Response({'status': 'Failed', 'error': 'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)

class UserLogoutView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            
            token.blacklist()
            return Response({"message": "Successfully logged out."}, status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class UserListAPIView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)


class PasswordChangeView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = PasswordChangeSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            user = request.user
            user.set_password(serializer.validated_data['new_password'])
            user.save()
            return Response({
                "status": "Success",
                "message": "Password updated successfully"
            }, status=status.HTTP_200_OK)
        return Response({
            "status": "Failed",
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

        
# class ForgotPasswordAPIView(APIView):
#     serializer_class = ForgotPasswordSerializer
    
#     def post(self, request):
#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid():
#             email = serializer.validated_data['email']
#             new_password = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
#             user = User.objects.get(email=email)
#             user.set_password(new_password)
#             user.save()
#             subject = 'New Password'
#             message = f'Your new password is: {new_password}'
#             # from_email = 'your-email@example.com' 
#             from_email = settings.DEFAULT_FROM_EMAIL
#             to_email = [email]

#             send_mail(subject, message, from_email, to_email)
            
            # return Response({
            #     "status": "Success",
            #     "message": "New password sent to your email."
            # }, status=status.HTTP_200_OK)
        
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class ForgotPasswordAPIView(APIView):
    serializer_class = ForgotPasswordSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            token = generate_token()
            expiration_time = token_expire_time()

            try:
                user = User.objects.get(email=email)
                cache.set(token, {'user_id': user.id, 'expires_at': expiration_time}, timeout=600)  # Cache token with 10 minutes expiry

                reset_password_link = f'http://example.com/reset_password/?token={token}'
                subject = 'Reset your password'
                message = f'Click the link to reset your password: {reset_password_link}'
                from_email = settings.DEFAULT_FROM_EMAIL
                to_email = [email]

                send_mail(subject, message, from_email, to_email)

                # return Response({'message': 'Password reset link sent to your email.'}, status=status.HTTP_200_OK)
                return Response({
                "status": "Success",
                "message": "Password reset link sent to your email."
            }, status=status.HTTP_200_OK)
            
            except User.DoesNotExist:
                return Response({
                "status": "Failed",
                "message": "User with this email does not exist."
            }, status=status.HTTP_404_NOT_FOUND)
                # return Response({'error': 'User with this email does not exist.'}, status=status.HTTP_404_NOT_FOUND)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PasswordResetView(APIView):
    serializer_class = PasswordResetSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        token = request.query_params.get('token')
        if not token:
            return Response({'error': 'Token is required.'}, status=status.HTTP_400_BAD_REQUEST)

        token_data = cache.get(token)
        if not token_data:
            return Response({'error': 'Token is invalid or has expired.'}, status=status.HTTP_400_BAD_REQUEST)

        if timezone.now() > token_data['expires_at']:
            return Response({'error': 'Token has expired.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(id=token_data['user_id'])
        except User.DoesNotExist:
            return Response({'error': 'Invalid token.'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user.set_password(serializer.validated_data['new_password'])
            user.save()

            cache.delete(token)  # Delete the token from cache

            # return Response({'message': 'Password has been reset successfully.'}, status=status.HTTP_200_OK)
            return Response({
                "status": "Success",
                "message": "Password has been reset successfully."
            }, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
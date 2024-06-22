from django.contrib.auth import authenticate
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from .models import CustomUser
from .serializers import UserSerializer, UserLoginSerializer
from rest_framework.permissions import IsAuthenticated
from .serializers import PasswordChangeSerializer






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

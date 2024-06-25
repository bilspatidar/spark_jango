from django.urls import path
from .views import UserRegisterView, UserLoginView, UserLogoutView, PasswordChangeView, ForgotPasswordAPIView, PasswordResetView

# router = DefaultRouter()
# router.register(r'users', CustomUserViewSet)

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('change_password/', PasswordChangeView.as_view(), name='change-password'),
    path('forgot_password/', ForgotPasswordAPIView.as_view(), name='forgot-password'),
    path('reset_password/', PasswordResetView.as_view(), name='reset_password'),
]

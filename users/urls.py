from django.urls import path
from .views import UserDetailView, UserListCreateView, UserLoginView, UserLogoutView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', UserListCreateView.as_view(), name='user-register'),
    path('<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('logout/', UserLogoutView.as_view(), name='user-logout'),
    path('password-reset', auth_views.PasswordResetView.as_view(), name='password-reset'),
    path('password-reset-done/', auth_views.PasswordResetDoneView.as_view(), name='password-reset-done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password-reset-confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password-reset-complete'),
]
from django.urls import path
from .views import CreateAlertView, ListAlertView, DeleteAlertView, LogoutView, UserregistrationView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('create/', CreateAlertView.as_view(), name='create_alert'),
    path('delete/<int:pk>/', DeleteAlertView.as_view(), name='delete_alert'),
    path('', ListAlertView.as_view(), name='list_alerts'),

    path('register/', UserregistrationView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name="token_refresh"),

    path('logout/', LogoutView.as_view(), name='logout'),
]

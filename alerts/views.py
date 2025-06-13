from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Alert
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import AlertSerializer, UserRegistrationSerializer
from django.core.cache import cache
import smtplib
from email.mime.text import MIMEText

# Create Alert View
class CreateAlertView(generics.CreateAPIView):
  queryset = Alert.objects.all()
  serializer_class = AlertSerializer
  permission_classes = [IsAuthenticated]

  def perform_create(self, serializer):
    serializer.save(user=self.request.user)

# DELETE ALERT VIEW
class DeleteAlertView(generics.DestroyAPIView):
  queryset = Alert.objects.all()
  serializer_class = AlertSerializer
  permission_classes = [IsAuthenticated]

  def get_queryset(self):
    return self.queryset.filter(user=self.request.user)
  

# LIST ALL ALERT VIEW
class ListAlertView(generics.ListAPIView):
  serializer_class = AlertSerializer
  permission_classes = [IsAuthenticated]

  def get_queryset(self):
    status_filter = self.request.query_params.get('status')
    queryset = Alert.objects.filter(user=self.request.user)
    if status_filter:
      queryset = queryset.filter(status=status_filter)
    return queryset
  
  def list(self, request, *args, **kwargs):
    cache_key = f'alerts_{request.user.id}'
    cache_data = cache.get(cache_key)
    if cache_data:
      return Response(cache_data)

    queryset = self.filter_queryset(self.get_queryset())
    page = self.paginate_queryset(queryset)
    if page is None:
      serializer = self.get_serializer(page, many=True)
      response = self.get_paginated_response(serializer.data)
      cache.set(cache_key, response.data, timeout=60)
      return Response
  
    serializer = self.get_serializer(queryset, many=True)
    response_data = serializer.data
    cache.set(cache_key, response_data, timeout=60)
    return Response(response_data)
  

class UserregistrationView(generics.CreateAPIView):
  serializer_class = UserRegistrationSerializer

class LogoutView(APIView):
  permission_classes = [IsAuthenticated]
  
  def post(self, request):
    try:
      refresh_token = request.data['refresh']
      token = RefreshToken(refresh_token)
      token.blacklist()
      return Response(status=status.HTTP_205_RESET_CONTENT)
    except Exception as e:
      return Response(status=status.HTTP_400_BAD_REQUEST)

# SEND EMAIL
def send_mail(to_email, cryptocurrency, target_price):
    msg = MIMEText(f"The price of {cryptocurrency} has reached {target_price}.")
    msg['Subject'] = 'Price Alert'
    msg['From'] = 'your-email@gmail.com'
    msg['To'] = to_email

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login('your-email@gmail.com', 'your-password')
        server.send_message(msg)
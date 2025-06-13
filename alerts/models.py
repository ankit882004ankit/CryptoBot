from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Alert(models.Model):
  STATUS = [
    ('created','Created'),
    ('deleted', 'Deleted'),
    ('tiggered', 'Triggered')
  ]

  user = models.ForeignKey(User, on_delete=models.CASCADE)
  cryptocurrency = models.CharField(max_length=50)
  target_price = models.DecimalField(max_digits=18, decimal_places=2)
  status = models.CharField(max_length=50, choices=STATUS, default='created')
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self) -> str:
    return f"{self.cryptocurrency} at {self.target_price} ({self.status}) created at {self.created_at}"
  

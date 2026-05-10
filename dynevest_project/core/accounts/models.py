from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class MiningPlan(models.Model):
    name = models.CharField(max_length=100)        # e.g., Silver Tier
    price = models.DecimalField(max_digits=10, decimal_places=2) # e.g., 500.00
    daily_roi = models.FloatField()               # e.g., 0.8%
    duration_days = models.IntegerField()         # e.g., 120
    hashrate = models.CharField(max_length=50)    # e.g., 15 TH/s

    def __str__(self):
        return self.name
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    mining_power = models.CharField(max_length=50, default="0 TH/s")
    
    def __str__(self):
        return f"{self.user.username}'s Profile"


class Transaction(models.Model):
    TRANSACTION_TYPES = (
        ('DEPOSIT', 'Deposit'),
        ('PURCHASE', 'Plan Purchase'),
        ('YIELD', 'Mining Yield'),
    )
    
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    timestamp = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.transaction_type} - {self.amount} ({self.profile.user.username})"   

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Wallet(models.Model):
    # This links the wallet to a User. If the User is deleted, the wallet is deleted.
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    # DecimalField is used for money because it is more accurate than Float
    deposit_balance = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    earnings_balance = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    
    def __str__(self):
        return f"{self.user.username}'s Wallet"

# This function is the "Light" that turns on
@receiver(post_save, sender=User)
def create_user_wallet(sender, instance, created, **kwargs):
    if created:
        # If a new user was just created, build their wallet automatically
        Wallet.objects.create(user=instance)

# This ensures the wallet stays synced if the user is updated
@receiver(post_save, sender=User)
def save_user_wallet(sender, instance, **kwargs):
    instance.wallet.save()

class MiningPlan(models.Model):
    name = models.CharField(max_length=100) # e.g., "Silver Tier"
    price = models.DecimalField(max_digits=10, decimal_places=2)
    daily_roi = models.DecimalField(max_digits=5, decimal_places=2) # e.g., 2.50 for 2.5%
    duration_days = models.IntegerField(default=30)
    
    def __str__(self):
        return self.name

class Transaction(models.Model):
    TRANSACTION_TYPES = (
        ('deposit', 'Deposit'),
        ('withdrawal', 'Withdrawal'),
        ('purchase', 'Plan Purchase'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    transaction_type = models.CharField(max_length=20, choices=TRANSACTION_TYPES)
    timestamp = models.DateTimeField(auto_now_add=True) # Automatically records the date/time
    status = models.CharField(max_length=20, default='pending') # pending, completed, failed

    def __str__(self):
        return f"{self.user.username} - {self.transaction_type} - {self.amount}"
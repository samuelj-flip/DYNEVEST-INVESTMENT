from django.contrib import admin
from .models import Wallet
from .models import Wallet, MiningPlan, Transaction  # Add MiningPlan here!

admin.site.register(Wallet)
admin.site.register(MiningPlan)
admin.site.register(Transaction) # Register it here

from django.contrib import admin
from .models import MiningPlan, Profile, Transaction

# Register your models here.
admin.site.register(MiningPlan)
admin.site.register(Profile)
admin.site.register(Transaction)
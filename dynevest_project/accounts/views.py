from django.shortcuts import render
from .models import MiningPlan, Transaction, Wallet

# The Main Overview Page
def index(request):
    # We grab the wallet to show the balance on the main dashboard
    wallet = Wallet.objects.get(user=request.user)
    return render(request, 'accounts/index.html', {'wallet': wallet})

# The Page where they buy plans
def plans_view(request):
    all_plans = MiningPlan.objects.all()
    return render(request, 'accounts/plans.html', {'plans': all_plans})

# The History Page
def transactions_view(request):
    my_history = Transaction.objects.filter(user=request.user)
    return render(request, 'accounts/transactions.html', {'transactions': my_history})

# The Profile Settings Page
def settings_view(request):
    return render(request, 'accounts/settings.html')
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse


def index_view(request):
    return render(request, 'landing/index.html')


@login_required
def dashboard_view(request):
    # Datos de saldo simulados (sin modelo por ahora)
    context = {
        'saldo': 12500,
        'usuario': request.user,
    }
    return render(request, 'wallet/dashboard.html', context)


@login_required
def deposit_view(request):
    if request.method == 'POST':
        monto = request.POST.get('monto')
        if monto:
            messages.success(request, f'¡Depósito de ${monto} realizado exitosamente!')
            return HttpResponseRedirect(reverse('dashboard'))
    return render(request, 'wallet/deposit.html')

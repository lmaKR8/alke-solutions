from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def transaction_list_view(request):
    # Datos de movimientos simulados (sin modelo por ahora)
    movimientos = [
        {'tipo': 'deposito', 'monto': 5000, 'descripcion': 'Depósito inicial', 'fecha': '2026-02-01'},
        {'tipo': 'envio', 'monto': 2000, 'descripcion': 'Pago a contacto', 'fecha': '2026-02-10'},
        {'tipo': 'recibido', 'monto': 3500, 'descripcion': 'Transferencia recibida', 'fecha': '2026-02-15'},
    ]
    context = {
        'movimientos': movimientos,
    }
    return render(request, 'transactions/transaction_list.html', context)

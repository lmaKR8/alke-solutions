from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse


@login_required
def contact_list_view(request):
    # Datos de contactos simulados (sin modelo por ahora)
    contactos = [
        {'nombre': 'Ana Torres', 'cbu': '0000003100010000000001', 'alias': 'ana.torres', 'banco': 'Banco Demo'},
        {'nombre': 'Luis Pérez', 'cbu': '0000003100010000000002', 'alias': 'luis.perez', 'banco': 'Banco Demo'},
    ]
    context = {
        'contactos': contactos,
    }
    return render(request, 'contacts/contact_list.html', context)


@login_required
def contact_form_view(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        cbu = request.POST.get('cbu')
        if nombre and cbu:
            messages.success(request, f'Contacto {nombre} agregado exitosamente.')
            return HttpResponseRedirect(reverse('contact_list'))
    return render(request, 'contacts/contact_form.html')


@login_required
def send_money_view(request):
    # Datos de contactos simulados para el formulario de envío
    contactos = [
        {'nombre': 'Ana Torres', 'cbu': '0000003100010000000001', 'alias': 'ana.torres'},
        {'nombre': 'Luis Pérez', 'cbu': '0000003100010000000002', 'alias': 'luis.perez'},
    ]
    if request.method == 'POST':
        contacto = request.POST.get('contacto')
        monto = request.POST.get('monto')
        if contacto and monto:
            messages.success(request, f'¡Dinero enviado exitosamente a {contacto} por ${monto}!')
            return HttpResponseRedirect(reverse('transaction_list'))
    context = {
        'contactos': contactos,
    }
    return render(request, 'contacts/send_money.html', context)

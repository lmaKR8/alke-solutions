# Alke Wallet — Billetera Digital con Django

## Índice

- [Autor](#autor)
- [Descripción del Proyecto](#descripción-del-proyecto)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Conceptos de Django Aplicados](#conceptos-de-django-aplicados)
- [Funcionalidades Implementadas](#funcionalidades-implementadas)
- [Uso del Sistema](#uso-del-sistema)
- [Testing](#testing)
- [Documentación Adicional](#documentación-adicional)

---

## Autor

**Desarrollado por**: Leandro Marchant A.  
**Tipo**: Proyecto Educativo
**Módulo**: Desarrollo Web con Django — Fundamentos (M6)  
**Programa**: Fullstack Python — Talento Digital  
**Año**: 2026

---

## Descripción del Proyecto

**Alke Wallet** es una aplicación web de billetera digital desarrollada con el framework Django como proyecto del módulo de Desarrollo Web con Django — Fundamentos del programa **Fullstack Python — Talento Digital 2026**.

Es una refactorización de [Alke Wallet (front-end)](https://github.com/lmaKR8/alke-wallet), originalmente construida con HTML5, CSS3, Bootstrap y JavaScript con persistencia en `localStorage`. Esta versión migra toda la lógica a un backend Django con autenticación real, sistema de templates con herencia y arquitectura modular.

### El Desafío

**Alke Solutions**, una empresa de desarrollo de software, necesita construir aplicaciones web utilizando Django. El objetivo es demostrar el dominio de las características fundamentales del framework:

- Configurar un proyecto Django funcional con múltiples aplicaciones
- Crear y registrar aplicaciones dentro del proyecto
- Implementar vistas que respondan a solicitudes HTTP
- Configurar URLs a nivel de proyecto y de aplicación
- Crear plantillas HTML con herencia de templates
- Integrar archivos estáticos (CSS, JS)
- Implementar autenticación de usuarios (login, registro, logout)
- Proteger vistas con `@login_required`

### Solución Implementada

Aplicación web modular con Django que implementa:

- **4 aplicaciones Django** bajo el directorio `apps/` (`accounts`, `wallet`, `transactions`, `contacts`)
- **Sistema de autenticación** completo con registro, login y logout
- **11 templates HTML** con herencia desde `base.html` y componentes reutilizables
- **Navegación condicional** que muestra opciones según el estado de autenticación
- **Vistas protegidas** con `@login_required` para usuarios autenticados
- **Framework de mensajes** de Django para feedback al usuario
- **Archivos estáticos** personalizados (CSS y JS)
- **Datos demo** hardcodeados para demostrar la funcionalidad sin modelos de base de datos

---

## Estructura del Proyecto

El proyecto está organizado siguiendo principios de modularización y separación de responsabilidades:

```
alke-solutions/
│
├── manage.py                              # Script de gestión de Django
├── requirements.txt                       # Dependencias del proyecto
├── db.sqlite3                             # Base de datos SQLite (desarrollo)
├── README.md                              # Este archivo
│
├── alke_wallet/                           # Configuración del proyecto Django
│   ├── __init__.py                            # Inicialización del módulo
│   ├── settings.py                            # Configuración principal
│   ├── urls.py                                # URLs raíz del proyecto
│   ├── wsgi.py                                # Configuración WSGI
│   └── asgi.py                                # Configuración ASGI
│
├── apps/                                  # Aplicaciones Django
│   ├── __init__.py                            # Inicialización del paquete
│   │
│   ├── accounts/                              # App de autenticación y usuarios
│   │   ├── __init__.py
│   │   ├── admin.py                               # Configuración del admin
│   │   ├── apps.py                                # Configuración de la app
│   │   ├── forms.py                               # RegisterForm (UserCreationForm)
│   │   ├── models.py                              # Modelos (vacío, usa User de Django)
│   │   ├── urls.py                                # Rutas: login, register, logout
│   │   ├── views.py                               # CustomLoginView, register_view
│   │   ├── tests.py                               # Pruebas de la app
│   │   └── migrations/                            # Migraciones de la BD
│   │
│   ├── wallet/                                # App de billetera (landing, dashboard, depósitos)
│   │   ├── __init__.py
│   │   ├── admin.py                               # Configuración del admin
│   │   ├── apps.py                                # Configuración de la app
│   │   ├── models.py                              # Modelos (placeholder)
│   │   ├── urls.py                                # Rutas: index, dashboard, deposit
│   │   ├── views.py                               # index_view, dashboard_view, deposit_view
│   │   ├── tests.py                               # Pruebas de la app
│   │   └── migrations/                            # Migraciones de la BD
│   │
│   ├── transactions/                          # App de transacciones (historial)
│   │   ├── __init__.py
│   │   ├── admin.py                               # Configuración del admin
│   │   ├── apps.py                                # Configuración de la app
│   │   ├── models.py                              # Modelos (placeholder)
│   │   ├── urls.py                                # Rutas: transaction_list
│   │   ├── views.py                               # transaction_list_view
│   │   ├── tests.py                               # Pruebas de la app
│   │   └── migrations/                            # Migraciones de la BD
│   │
│   └── contacts/                              # App de contactos y envío de dinero
│       ├── __init__.py
│       ├── admin.py                               # Configuración del admin
│       ├── apps.py                                # Configuración de la app
│       ├── models.py                              # Modelos (placeholder)
│       ├── urls.py                                # Rutas: contact_list, contact_create, send_money
│       ├── views.py                               # contact_list_view, contact_form_view, send_money_view
│       ├── tests.py                               # Pruebas de la app
│       └── migrations/                            # Migraciones de la BD
│
├── templates/                             # Templates globales
│   ├── base.html                              # Template base (Bootstrap 5.3.2)
│   ├── includes/                              # Fragmentos reutilizables
│   │   ├── _navbar.html                           # Barra de navegación condicional
│   │   ├── _footer.html                           # Footer común
│   │   └── _alerts.html                           # Alertas del framework de mensajes
│   ├── landing/
│   │   └── index.html                             # Landing page pública
│   ├── accounts/
│   │   ├── login.html                             # Página de inicio de sesión
│   │   └── register.html                          # Página de registro
│   ├── wallet/
│   │   ├── dashboard.html                         # Dashboard con saldo y accesos rápidos
│   │   └── deposit.html                           # Formulario de depósito
│   ├── transactions/
│   │   └── transaction_list.html                  # Historial de transacciones
│   └── contacts/
│       ├── contact_list.html                      # Lista de contactos
│       ├── contact_form.html                      # Formulario crear contacto
│       └── send_money.html                        # Formulario enviar dinero
│
├── static/                                # Archivos estáticos
│   ├── css/
│   │   └── style.css                          # Estilos personalizados (variables CSS)
│   ├── js/
│   │   └── main.js                            # JS mínimo (tooltips Bootstrap)
│   └── img/                                   # Imágenes (placeholder)
│
├── docs/                                  # Documentación del proyecto
│   ├── instrucciones.md                       # Análisis AS-IS y arquitectura TO-BE
│   ├── requerimientos.md                      # Requerimientos del módulo
│   ├── plan-desarrollo.md                     # Plan paso a paso de implementación
│   ├── convenciones-git.md                    # Convenciones de commits y ramas
│   ├── README-ejemplo.md                      # README de ejemplo (referencia)
│   └── django_docs/                           # Documentación de referencia Django
│
└── env/                                   # Entorno virtual de Python
```

---

## Conceptos de Django Aplicados

### 1. **Configuración del Proyecto**

- Proyecto creado con `django-admin startproject alke_wallet`
- Configuración de idioma español Chile (`es-cl`) y zona horaria `America/Santiago`
- Templates globales configurados en `TEMPLATES[0]['DIRS']`
- Archivos estáticos configurados con `STATICFILES_DIRS`
- Redirecciones de autenticación configuradas: `LOGIN_URL`, `LOGIN_REDIRECT_URL`, `LOGOUT_REDIRECT_URL`

**Ejemplo:**

```python
# alke_wallet/settings.py
LANGUAGE_CODE = 'es-cl'
TIME_ZONE = 'America/Santiago'

TEMPLATES = [{
    'DIRS': [BASE_DIR / 'templates'],
    ...
}]

STATICFILES_DIRS = [BASE_DIR / 'static']

LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'dashboard'
LOGOUT_REDIRECT_URL = 'login'
```

### 2. **Estructura y Aplicaciones**

- 4 aplicaciones creadas bajo el directorio `apps/` para mantener organización limpia
- Cada app registrada en `INSTALLED_APPS` con prefijo `apps.`
- `apps.py` de cada aplicación configurado con `name = 'apps.<nombre_app>'`

**Aplicaciones:**

```
apps/
├── accounts       → Autenticación (login, registro, logout)
├── wallet         → Billetera (landing, dashboard, depósitos)
├── transactions   → Historial de transacciones
└── contacts       → Gestión de contactos y envío de dinero
```

### 3. **Vistas y Rutas (URLs)**

- URLs configuradas a **dos niveles**: proyecto (`alke_wallet/urls.py`) y aplicación (`apps/<app>/urls.py`)
- Uso de `include()` para delegar rutas a cada app
- Combinación de **vistas basadas en funciones (FBV)** y **vistas basadas en clases (CBV)**
- Rutas con nombres (`name=`) para referencias con `{% url %}` en templates

**Ejemplo de URLs del proyecto:**

```python
# alke_wallet/urls.py
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.wallet.urls')),
    path('accounts/', include('apps.accounts.urls')),
    path('transactions/', include('apps.transactions.urls')),
    path('contacts/', include('apps.contacts.urls')),
]
```

### 4. **Templates y Herencia**

- Template base (`base.html`) con Bootstrap 5.3.2 CDN
- Sistema de **bloques** (`{% block %}`) para contenido dinámico: `title`, `content`, `extra_css`, `extra_js`
- **Includes** para componentes reutilizables: `_navbar.html`, `_footer.html`, `_alerts.html`
- Todos los templates extienden de `base.html` con `{% extends 'base.html' %}`
- Uso de `{% load static %}` para referenciar archivos estáticos

**Jerarquía de herencia:**

```
base.html
    ├── includes/_navbar.html    ({% include %})
    ├── includes/_alerts.html    ({% include %})
    ├── includes/_footer.html    ({% include %})
    │
    ├── landing/index.html       ({% extends 'base.html' %})
    ├── accounts/login.html      ({% extends 'base.html' %})
    ├── accounts/register.html   ({% extends 'base.html' %})
    ├── wallet/dashboard.html    ({% extends 'base.html' %})
    ├── wallet/deposit.html      ({% extends 'base.html' %})
    ├── transactions/transaction_list.html
    └── contacts/contact_list.html, contact_form.html, send_money.html
```

### 5. **Archivos Estáticos**

- CSS personalizado con **variables CSS** para paleta de colores consistente
- JavaScript mínimo para inicialización de tooltips de Bootstrap
- Archivos servidos desde `static/` con `{% static %}` tag

**Variables CSS:**

```css
:root {
  --color-primario: #0d6efd;
  --color-exito: #198754;
  --color-peligro: #dc3545;
  --color-advertencia: #ffc107;
  --color-oscuro: #212529;
  --color-fondo: #f8f9fa;
}
```

### 6. **Autenticación de Usuarios**

- `CustomLoginView` extiende `LoginView` de Django (CBV) con mensaje de bienvenida
- `register_view` (FBV) con formulario personalizado `RegisterForm(UserCreationForm)`
- `LogoutView` genérica de Django con protección CSRF
- Decorador `@login_required` en todas las vistas protegidas

**Ejemplo:**

```python
class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f'¡Bienvenido {self.request.user.first_name}!')
        return response
```

### 7. **Framework de Mensajes**

- Uso de `django.contrib.messages` para notificaciones al usuario
- Mensajes de éxito en login, registro, depósito, contacto y envío de dinero
- Renderizado en `_alerts.html` con estilos Bootstrap (`alert-success`, `alert-danger`, etc.)
- Cierre con botón dismiss de Bootstrap

---

## Funcionalidades Implementadas

### 1. Landing Page

- Página pública de presentación de Alke Wallet
- Descripción del servicio con cards informativas (Depósitos, Transferencias, Historial)
- Botones condicionales: **Crear cuenta / Iniciar sesión** (no autenticado) o **Ir al Dashboard** (autenticado)
- Ruta: `GET /`

### 2. Registro de Usuario

- Formulario con campos: username, email, password1, password2
- Validación automática de contraseñas (Django `UserCreationForm`)
- Login automático tras registro exitoso
- Redirección al dashboard con mensaje de bienvenida
- Ruta: `GET/POST /accounts/register/`

### 3. Inicio de Sesión

- Formulario de autenticación con username y password
- Redirección automática al dashboard si ya está autenticado
- Mensaje de bienvenida personalizado con el nombre del usuario
- Ruta: `GET/POST /accounts/login/`

### 4. Cierre de Sesión

- Logout seguro vía `POST` con protección CSRF
- Redirección a la página de login
- Ruta: `POST /accounts/logout/`

### 5. Dashboard

- Panel principal con saldo disponible (dato demo: $12.500)
- Accesos rápidos a: Depositar, Enviar dinero, Transacciones, Contactos
- Saludo personalizado con el username
- Protegido con `@login_required`
- Ruta: `GET /dashboard/`

### 6. Depósito de Fondos

- Formulario con monto y descripción
- Mensaje de confirmación tras envío del formulario
- Redirección al dashboard
- Protegido con `@login_required`
- Ruta: `GET/POST /deposit/`

### 7. Historial de Transacciones

- Tabla con columnas: Tipo, Monto, Descripción, Fecha
- Badges de color según tipo: Depósito (verde), Envío (rojo), Recibido (celeste)
- Datos demo: 3 transacciones de ejemplo
- Protegido con `@login_required`
- Ruta: `GET /transactions/`

### 8. Lista de Contactos

- Tabla con columnas: Nombre, CBU, Alias, Banco
- Botón para agregar nuevo contacto
- Datos demo: 2 contactos de ejemplo
- Protegido con `@login_required`
- Ruta: `GET /contacts/`

### 9. Crear Contacto

- Formulario con campos: Nombre, CBU (22 dígitos), Alias, Banco
- Mensaje de confirmación tras guardar
- Redirección a la lista de contactos
- Protegido con `@login_required`
- Ruta: `GET/POST /contacts/new/`

### 10. Enviar Dinero

- Selector de contacto desde lista disponible
- Campos: monto a enviar y mensaje opcional
- Mensaje de confirmación con nombre del contacto y monto
- Redirección al historial de transacciones
- Protegido con `@login_required`
- Ruta: `GET/POST /contacts/send/`

### 11. Navegación Condicional

- **Usuario autenticado**: Dashboard, Depositar, Transacciones, Contactos, Enviar dinero, nombre de usuario, botón Cerrar sesión
- **Usuario no autenticado**: Iniciar sesión, Registrarse
- Navbar responsive con toggler para móviles

---

## Uso del Sistema

### Requisitos

- **Python**: 3.12 o superior
- **Django**: 6.0.2
- **Dependencias adicionales**: `asgiref`, `sqlparse`, `tzdata` (instaladas con Django)

### Instalación

```bash
# 1. Clonar el repositorio
git clone <url-del-repositorio>
cd alke-solutions

# 2. Crear entorno virtual
python -m venv env

# 3. Activar entorno virtual
# Windows:
env\Scripts\activate
# Linux/Mac:
source env/bin/activate

# 4. Instalar dependencias
pip install -r requirements.txt

# 5. Ejecutar migraciones
python manage.py migrate

# 6. Crear superusuario (opcional, para acceso al admin)
python manage.py createsuperuser
```

### Ejecución

```bash
# Iniciar el servidor de desarrollo
python manage.py runserver
```

Acceder en el navegador a: `http://127.0.0.1:8000/`

### Flujo de Uso

1. **Landing Page** (`/`)
   - Página de bienvenida con descripción del servicio
   - Opciones para crear cuenta o iniciar sesión

2. **Registro** (`/accounts/register/`)
   - Crear una nueva cuenta con username, email y contraseña
   - Login automático tras registro exitoso

3. **Login** (`/accounts/login/`)
   - Iniciar sesión con credenciales existentes

4. **Dashboard** (`/dashboard/`)
   - Vista principal con saldo y accesos rápidos

5. **Operaciones**
   - Depositar fondos desde `/deposit/`
   - Ver historial en `/transactions/`
   - Gestionar contactos en `/contacts/`
   - Enviar dinero desde `/contacts/send/`

6. **Cerrar sesión**
   - Botón en la barra de navegación

### Panel de Administración

Acceder a `http://127.0.0.1:8000/admin/` con las credenciales del superusuario para gestionar usuarios y datos del sistema.

---

## Mapa de Rutas

```
| Ruta                    | Vista                  | Template                            | Name              | Protegida |
| ----------------------- | ---------------------- | ----------------------------------- | ----------------- | --------- |
| `/`                     | `index_view`           | `landing/index.html`                | `index`           | No        |
| `/dashboard/`           | `dashboard_view`       | `wallet/dashboard.html`             | `dashboard`       | Sí        |
| `/deposit/`             | `deposit_view`         | `wallet/deposit.html`               | `deposit`         | Sí        |
| `/accounts/login/`      | `CustomLoginView`      | `accounts/login.html`               | `login`           | No        |
| `/accounts/register/`   | `register_view`        | `accounts/register.html`            | `register`        | No        |
| `/accounts/logout/`     | `LogoutView`           | —                                   | `logout`          | Sí        |
| `/transactions/`        | `transaction_list_view`| `transactions/transaction_list.html`| `transaction_list`| Sí        |
| `/contacts/`            | `contact_list_view`    | `contacts/contact_list.html`        | `contact_list`    | Sí        |
| `/contacts/new/`        | `contact_form_view`    | `contacts/contact_form.html`        | `contact_create`  | Sí        |
| `/contacts/send/`       | `send_money_view`      | `contacts/send_money.html`          | `send_money`      | Sí        |
| `/admin/`               | Django Admin           | —                                   | —                 | Sí        |
```

---

## Testing

### Ejecutar Tests

```bash
# Ejecutar todos los tests
python manage.py test

# Ejecutar tests de una app específica
python manage.py test apps.accounts
python manage.py test apps.wallet
python manage.py test apps.transactions
python manage.py test apps.contacts

# Ejecutar con verbose
python manage.py test --verbosity=2
```

---

## Tecnologías Utilizadas

```
| Tecnología        | Versión  | Propósito                               |
| ----------------- | -------- | --------------------------------------- |
| **Python**        | 3.12+   | Lenguaje backend                         |
| **Django**        | 6.0.2   | Framework web principal                  |
| **SQLite**        | —       | Base de datos para desarrollo            |
| **Bootstrap**     | 5.3.2   | Framework CSS (CDN)                      |
| **HTML5**         | —       | Estructura de templates                  |
| **CSS3**          | —       | Estilos personalizados                   |
| **JavaScript**    | ES6+    | Interactividad mínima (tooltips)         |
```

---

## Características Técnicas

### Buenas Prácticas Implementadas

**Separación de responsabilidades**

- 4 aplicaciones independientes con responsabilidades claras
- Templates organizados por app
- Archivos estáticos centralizados

**Herencia de templates**

- Template base reutilizable con bloques dinámicos
- Componentes incluidos (`_navbar`, `_footer`, `_alerts`)
- Código DRY (Don't Repeat Yourself)

**Seguridad**

- Protección CSRF en todos los formularios (`{% csrf_token %}`)
- Vistas protegidas con `@login_required`
- Validación de contraseñas con validators de Django
- Logout vía POST (no GET) para evitar CSRF

**Configuración adecuada**

- Idioma y zona horaria configurados para Chile
- URLs con nombres para desacoplamiento de templates
- Redirecciones de autenticación configuradas en `settings.py`

**Código limpio y legible**

- Nombres descriptivos en español para contexto educativo
- Comentarios explicativos en vistas
- Estructura de carpetas consistente

---

## Limitaciones Conocidas

### Estado Actual (M6 — Fundamentos)

- **Sin modelos personalizados**: Los datos de saldo, transacciones y contactos son demo (hardcodeados en las vistas). Los modelos están como placeholder (`# Create your models here.`)
- **Sin persistencia de operaciones**: Los formularios de depósito, contacto y envío de dinero muestran mensajes de confirmación pero no guardan datos en la base de datos
- **Sin API REST**: La aplicación solo funciona vía templates (server-side rendering)
- **Sin paginación**: Las listas no implementan paginación
- **Sin búsqueda/filtros**: El historial de transacciones no tiene filtros funcionales
- **Sin soporte multi-moneda**: Solo muestra valores en CLP (pesos chilenos)

### Evolución Futura

Estas limitaciones serán abordadas en módulos posteriores del programa, donde se implementarán:

- Modelos de base de datos con ORM de Django
- Operaciones CRUD completas con persistencia
- API REST con Django REST Framework
- Paginación y filtros funcionales

---

## Licencia

Este proyecto es de uso educativo y no tiene licencia comercial.
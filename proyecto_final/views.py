from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render
from django.conf import settings

def skip_authentication(view_func):
    def wrapper(request, *args, **kwargs):
        if not settings.SKIP_AUTHENTICATION:
            # Si la autenticación está habilitada, redirigir a la página de inicio de sesión
            # o manejar de alguna manera la falta de autenticación.
            return HttpResponse("Autenticación requerida. Puedes personalizar este mensaje.")
        return view_func(request, *args, **kwargs)
    return wrapper

@skip_authentication
def bienvenida_campeones(request):
    respuesta_http = render(
        request=request,
        template_name='inicio.html',
        context={},
    )
    return respuesta_http

@skip_authentication
def acerca_de(request):
    respuesta_http = render(
        request=request,
        template_name='about.html',
        context={},
    )
    return respuesta_http

from django.contrib import admin
from django.urls import path, include

from blog.views import (
    crear_campeones, listar_campeoness, mostrar_campeones, borrar_campeones, editar_campeones,
)

urlpatterns = [
    # URLS de cursos
    path('wall/', listar_campeoness, name="wall"),
    path('crear_campeones/', crear_campeones, name="crear_campeones"),
    path('detalle_campeones/<int:id>', mostrar_campeones, name="mostrar_campeones"),
    path('editar_campeones/<int:id>', editar_campeones, name='editar_campeones'),
    path('borrar_campeones/<int:id>', borrar_campeones, name='borrar_campeones'),
]
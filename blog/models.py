from django.db import models
from django.contrib.auth.models import User

class Articulo(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='campeones_creados', null=True)
    titulo = models.CharField(max_length=150)
    subtitulo = models.CharField(max_length=100)
    cuerpo = models.TextField()  
    fecha = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(upload_to='campeones_img', null=True, blank=True)

    def __str__(self):
        return f"{self.titulo}, {self.subtitulo}, {self.cuerpo}"

from django.test import TestCase
from blog.models import Articulo
from django.contrib.auth.models import User
import datetime
from datetime import timezone

class ArticuloTests(TestCase):
    def test_creacion_articulo(self):
        
        user = User(
            username = 'Nico1407',
            first_name = 'Nicolas',
            last_name = 'Yospe',
            email = 'yospenicolas@gmail.com',
        )
        user.save()

        expectedDate = datetime.datetime.now(timezone.utc)

        articulo = Articulo(
            autor = user,
            titulo = 'Messi, el campeón',
            subtitulo = 'La Copa del Mundo, la obsesión',
            cuerpo = 'El sueño de un gigante',
            imagen = 'campeones_img/Messi_espalda.jpg',
        )
        articulo.save()

        # Compruebo que el curso fue creado y la data fue guardad correctamente
        self.assertEqual(Articulo.objects.count(), 1)
        self.assertEqual(articulo.autor.username, 'Nico1407')
        self.assertEqual(articulo.titulo, 'Messi, el campeón')
        self.assertEqual(articulo.subtitulo, 'La Copa del Mundo, la obsesión')
        self.assertEqual(articulo.cuerpo, 'El sueño de un gigante')
        self.assertEqual(articulo.fecha, expectedDate)
        self.assertEqual(articulo.imagen, 'campeones_img/Messi_espalda.jpg')

    def test_articulo_str(self):
        user = User(
            username = 'Nico1407',
            first_name = 'Nicolas',
            last_name = 'Yospe',
            email = 'yospenicolas@gmail.com',
        )
        user.save()

        expectedDate = datetime.datetime.now()

        articulo = Articulo(
            autor = user,
            titulo = 'Messi, el campeón',
            subtitulo = 'La Copa del Mundo, la obsesión',
            cuerpo = 'El sueño de un gigante',
            imagen = 'campeones_img/Messi_espalda.jpg'
            )
        articulo.save()

        
        self.assertEqual(articulo.__str__(), "Messi, el campeón, La Copa del Mundo, la obsesión, El sueño de un gigante,")
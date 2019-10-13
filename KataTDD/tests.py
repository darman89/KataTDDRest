from django.test import TestCase
from .models import Portafolio, User, Imagen
import json
from django.contrib.auth import authenticate


# Create your tests here.


class PortafolioTestCase(TestCase):

    def test_list_portafolios(self):
        url = '/portafolio/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)

    def test_count_images_list(self):
        user_model = User.objects.create_user(username='test', password='kd8wke-DE34', first_name='test',
                                              last_name='test', email='test@test.com',
                                              foto="test", perfil="test")
        Portafolio.objects.create(titulo="test1", usuario=user_model)
        Portafolio.objects.create(titulo="test2", usuario=user_model)

        response = self.client.get('/portafolio/')
        current_data = json.loads(response.content)
        print(current_data)
        self.assertEqual(len(current_data), 2)

    def test_get_info_user(self):
        response = self.client.post('/portafolio/addUser/', json.dumps(
            {"username": "test", "first_name": "test", "last_name": "test", "password": "AnyPas#5",
             "email": "test@test.com", "foto": "test", "perfil": "test"}), content_type='application/json')
        current_data = json.loads(response.content)
        self.assertEqual(current_data[0]['fields']['username'], 'test')

    def test_view_public_info(self):
        user_model = User.objects.create_user(username='test', password='kd8wke-DE34', first_name='test',
                                              last_name='test', email='test@test.com',
                                              foto="test", perfil="test")
        portafolio = Portafolio.objects.create(titulo="test1", usuario=user_model)
        Imagen.objects.create(titulo="test1Image", enlace='http://localhost/image1', descripcion='testImage-1',
                              tipo='gif', es_publica=True, portafolio=portafolio)
        Imagen.objects.create(titulo="test2Image", enlace='http://localhost/image2', descripcion='testImage-2',
                              tipo='gif', es_publica=False, portafolio=portafolio)

        response = self.client.get('/portafolio/getInfo/' + str(user_model.id))
        current_data = json.loads(response.content)
        self.assertEqual(current_data[0]['images'][0]['es_publica'], True)
        self.assertEqual(len(current_data[0]['images']), 1)

    def test_login(self):
        user_model = User.objects.create_user(username='test', password='kd8wke-DE34', first_name='test',
                                              last_name='test', email='test@test.com',
                                              foto="test", perfil="test")
        response = self.client.post('/portafolio/login/', json.dumps(
            {"username": user_model.username, "password": 'kd8wke-DE34'}), content_type='application/json')
        current_data = json.loads(response.content)
        self.assertEqual(current_data['status'], 'Authenticated')

    def test_edit_user(self):
        user_model = User.objects.create_user(username='test', password='kd8wke-DE34', first_name='test',
                                              last_name='test', email='test@test.com',
                                              foto="test", perfil="test")

        self.client.login(username=user_model.username, password='kd8wke-DE34')

        user = {"first_name": 'prueba edicion', "foto": 'fotonueva'}
        response = self.client.post('/portafolio/profile/', json.dumps(user), content_type='application/json')
        current_data = json.loads(response.content)
        self.assertEqual(current_data[0]['fields']['first_name'], 'prueba edicion')
        self.assertEqual(current_data[0]['fields']['foto'], 'fotonueva')



from django.test import TestCase
from .models import Portafolio, User
import json

# Create your tests here.


class PortafolioTestCase(TestCase):

    def test_list_portafolios(self):
        url = '/portafolio/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)

    def test_count_images_list(self):
        user_model = User.objects.create_user(username='test', password='kd8wke-DE34', first_name='test', last_name='test', email='test@test.com',
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



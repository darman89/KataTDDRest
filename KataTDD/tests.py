from django.test import TestCase


# Create your tests here.


class PortafolioTestCase(TestCase):

    def test_list_portafolios(self):
        url = '/portafolio/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)

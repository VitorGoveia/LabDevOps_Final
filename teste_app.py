import unittest
from app import app
import werkzeug

werkzeug
if not hasattr(werkzeug, '__version__'):
    werkzeug.__version__ = "mock-version"
class APITestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Criação do cliente de teste
        cls.client = app.test_client()

    def teste_rotas_items(self):
        response = self.client.get('/items')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"items":['item1', 'item2', 'item3']})

    def teste_rota_GET_login(self):
        response = self.client.get('/login')
        self.assertEqual(response.status_code, 405)
    
    def teste_protected_com_token(self):
        login_response = self.client.post('/login')
        token = login_response.json['access_token'] 
        headers = {
            'Authorization': f'Bearer {token}'
        }

        response = self.client.get('/protected', headers=headers)
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
import unittest
import requests

class ApiTest(unittest.TestCase):
#Validamos que la respuesta del request sea un 200
    def test_1_PruebaResponse(self):
        seguro = "http://127.0.0.1:4000/seguro"
        r = requests.get(seguro)
        self.assertEqual(r.status_code, 200)


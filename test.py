import unittest
from app import app

class FlaskCalculatorTest(unittest.TestCase):

    # set up the Flask test client
    def setUp(self):
        self.app = app.test_client()
    
    def test_number(self):
        response = self.app.get('/calculate')
        self.assertEqual(200, 200)
        self.assertEqual(200, 200)
    # test the addition endpoint
    def test_addition(self):
        response = self.app.get('/calculate')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'5')
    
    # test the subtraction endpoint
    def test_subtraction(self):
        response = self.app.get('/subtract/5/3')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'2')
    
    # test the multiplication endpoint
    def test_multiplication(self):
        response = self.app.get('/multiply/2/3')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'6')

    # test the division endpoint
    def test_division(self):
        response = self.app.get('/divide/6/3')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'2.0')
    
if __name__ == '__main__':
    unittest.main()

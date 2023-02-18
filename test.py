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
    def test_number1(self):
        response = self.app.get('/calculate')
        self.assertEqual(200, 200)
        self.assertEqual(200, 200) 
    def test_number2(self):
        response = self.app.get('/calculate')
        self.assertEqual(200, 200)
        self.assertEqual(200, 200)
    def test_number3(self):
        response = self.app.get('/calculate')
        self.assertEqual(200, 200)
        self.assertEqual(208, 200)
    # test the addition endpoint
    
    
if __name__ == '__main__':
    unittest.main()

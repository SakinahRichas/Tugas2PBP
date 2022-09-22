from django.test import TestCase, Client

# Create your tests here.
class Test(TestCase):
    def html_test(self):
        response = Client().get('/mywatchlist/html/')
        self.assertEqual(response.status_code,200)
    
    def xml_test(self):
        response = Client().get('/mywatchlist/xml/')
        self.assertEqual(response.status_code,200)
    
    def json_test(self):
        response = Client().get('/mywatchlist/json/')
        self.assertEqual(response.status_code,200)
    
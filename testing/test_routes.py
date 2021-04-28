import unittest
from main import app


class FlaskTest(unittest.TestCase):

    
    def setUp(self):
        app.config['TESTING'] = True

    def test_index_route(self):
        """
        Check for response 200 on the index page
        """
        tester = app.test_client()
        response = tester.get('/')
        status_code = response.status_code
        self.assertEqual(status_code, 200)

    def test_index_loads(self):
        """
        Checks that the home route '/' loads properly by checking for some page text of home.html in response data
        """
        tester = app.test_client()
        response = tester.get('/')
        self.assertTrue(b'wish to shorten.' in response.data)


    def test_results_get(self):
        """
        Asserts true of a status code of 302, showing there has been a redirect as this page should only be accessed through POST of forum in home.html
        """
        tester = app.test_client()
        response = tester.get('/results')
        status_code = response.status_code
        self.assertEqual(status_code, 302)
    
    def test_results_post(self):
        """
        Asserts true of a status code of 200, showing the page has successfully been served after a POST request was made.
        """
        tester = app.test_client()
        response = tester.post('/results', data={'urlName' : 'google.com'})
        status_code = response.status_code
        self.assertEqual(status_code, 200)
        
    
    def test_results_loads(self):
        """
        Checks that the results route '/results/' loads properly (after a successful POST) by checking for some page text of results.html in response data
        """
        tester = app.test_client()
        response = tester.post('/results', data={'urlName' : 'google.com'})
        
        self.assertTrue(b'Your shortened URL is:' in response.data)
    
    
    def test_false_route(self):
        """
        Checks for 404  response on a route that does not exist
        """
        tester = app.test_client()
        response = tester.get('/short/test')
        status_code = response.status_code
        self.assertEqual(status_code, 404)
        
if __name__ == "__main__":
    unittest.main()
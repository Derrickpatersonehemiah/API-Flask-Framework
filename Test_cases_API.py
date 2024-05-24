import unittest
from API_Test import app

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        # This sets up the Flask test client
        self.app = app.test_client()
        self.app.testing = True

    def test_get_static_response_success(self):
        # Test for a successful response
        response = self.app.get('/api')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/json')
        self.assertEqual(response.json, {
            "message": "Hi, Task 4.2 completed succesfully!",
            "status": "success"
        })

    def test_404_error(self):
        # Test for a 404 error for an undefined route
        response = self.app.get('/undefined_route')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.content_type, 'application/json')
        self.assertEqual(response.json, {
            "message": "Resource not found.",
            "status": "error"
        })

    def test_method_not_allowed(self):
        # Test for method not allowed (POST instead of GET)
        response = self.app.post('/api')
        self.assertEqual(response.status_code, 405)
        
    def test_environment_development(self):
        # Test environment specific settings, explicitly set DEBUG mode to True
        app.config['DEBUG'] = True
        self.assertTrue(app.config['DEBUG'])

    def test_internal_server_error(self):
        # Test for a 500 Internal Server Error
        response = self.app.get('/error')
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.content_type, 'application/json')
        self.assertEqual(response.json, {
            "message": "simulated server error.",
            "status": "error"
        })

    def test_forbidden_error(self):
        # Test for a 403 Forbidden Error
        response = self.app.get('/forbidden')
        self.assertEqual(response.status_code, 403)
        self.assertEqual(response.content_type, 'application/json')
        self.assertEqual(response.json, {
            "message": "simulated forbidden error.",
            "status": "error"
        })

if __name__ == '__main__':
    unittest.main()
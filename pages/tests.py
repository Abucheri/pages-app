from django.test import TestCase, SimpleTestCase  # We’re using SimpleTestCase here since we aren’t using a database

# Create your tests here.
class SimpleTests(SimpleTestCase):
	def test_home_page_status_code(self):
		response = self.client.get('/')
		self.assertEqual(response.status_code, 200)

	def test_about_page_status_code(self):
		response = self.client.get('/about/')
		self.assertEqual(response.status_code, 200)

from django.test import SimpleTestCase


class PagesTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/pages/")
        self.assertEqual(response.status_code, 200)

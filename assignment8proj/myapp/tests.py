from django.test import TestCase


class HomeViewTestCase(TestCase):
    def test_home_view(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Hello, World! This is my first Django app.")

class AboutViewTestCase(TestCase):
    def test_about_view(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "About Us\nThis is the about page of my Django app.")

class InformationViewTestCase(TestCase):
    def test_information_view(self):
        response = self.client.get('/information/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Information\nThis is the Information page for my Django app.")
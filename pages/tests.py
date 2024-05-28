from django.test import SimpleTestCase
from django.urls import reverse

class HomePagetests(SimpleTestCase):
    def test_urls_exist_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
    
    def test_urls_available_by_name(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_template_content(self):
        response = self.client.get(reverse("home"))
        self.assertContains(response, "<H1>HomePage</H1>")


class AboutPagetests(SimpleTestCase):
    def test_urls_exist_at_correct_location(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)

    def test_urls_available_by_name(self):
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)

    def test_template_content(self):
        response = self.client.get(reverse("about"))
        self.assertContains(response, "<H1>About page</H1>")

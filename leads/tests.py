from audioop import reverse
from django.test import TestCase
from django.shortcuts import reverse

class HomePageTest(TestCase):

    def test_status_code(self):
        response = self.client.get(reverse("landing-page"))
        self.assertEqual(response.status_code, 200)

    def test_template_name(self):
        response = self.client.get(reverse("landing-page"))
        self.assertTemplateUsed(response, "landing.html")
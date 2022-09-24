from django.test import TestCase

from events.models import *
from django.urls import reverse

@classmethod
class Error404ViewTest(TestCase):

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get("events/templates/error404")
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accesible_by_name(self):
        resp = self.client.get(reverse("error404"))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse("error404"))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, "events/templates/error404.html")

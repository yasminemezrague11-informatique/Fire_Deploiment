from django.test import TestCase
from django.urls import reverse
from .models import Incendie  # Corrigé ici : importé depuis models, pas forms

class IncendieApiTest(TestCase):
    def setUp(self):
        Incendie.objects.create(
            latitude=48.8566,
            longitude=2.3522,
            description="Feu à Paris",
            type="Feu de forêt",
            severity="Grave"
        )

    def test_get_incendies_api(self):
        response = self.client.get(reverse('incendies_api'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()['incendies']), 1)
        self.assertEqual(response.json()['incendies'][0]['description'], "Feu à Paris")

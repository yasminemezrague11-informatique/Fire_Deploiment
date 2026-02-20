from django.test import TestCase
from home.models import Citoyen, FireIncident, Incendie

class CitoyenModelTest(TestCase):
    def test_create_citoyen(self):
        citoyen = Citoyen.objects.create(
            fullname="Jean Dupont",
            email="jean.dupont@example.com",
            phone="0612345678",
            password="password123"
        )
        self.assertEqual(Citoyen.objects.count(), 1)
        self.assertEqual(citoyen.fullname, "Jean Dupont")

    def test_email_unique_constraint(self):
        Citoyen.objects.create(
            fullname="Jean Dupont",
            email="jean.dupont@example.com",
            phone="0612345678",
            password="password123"
        )
        with self.assertRaises(Exception):
            Citoyen.objects.create(
                fullname="Marie Curie",
                email="jean.dupont@example.com",  # Email déjà utilisé
                phone="0698765432",
                password="password456"
            )

class FireIncidentModelTest(TestCase):
    def test_create_fire_incident(self):
        fire_incident = FireIncident.objects.create(
            reporter_name="John Smith",
            contact_number="0612345678",
            address="123 Rue de Paris",
            fire_type="Forest Fire",
            fire_severity="High"
        )
        self.assertEqual(FireIncident.objects.count(), 1)
        self.assertEqual(fire_incident.reporter_name, "John Smith")

class IncendieModelTest(TestCase):
    def test_create_incendie(self):
        incendie = Incendie.objects.create(
            latitude=48.8566,
            longitude=2.3522,
            description="Feu à Paris",
            type="Feu de forêt",
            severity="Grave"
        )
        self.assertEqual(Incendie.objects.count(), 1)
        self.assertEqual(incendie.description, "Feu à Paris")

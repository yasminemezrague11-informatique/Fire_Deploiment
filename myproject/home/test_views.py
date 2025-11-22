from django.test import TestCase
from home.forms import CitoyenForm
from home.models import Citoyen
from django.contrib.auth import get_user_model

class CitoyenFormTest(TestCase):
    def test_valid_form(self):
        form_data = {
            'fullname': 'Jean Dupont',
            'email': 'jean.dupont@example.com',
            'phone': '0612345678',
            'password': 'password123',
            'confirmPassword': 'password123'
        }
        form = CitoyenForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_email(self):
        form_data = {
            'fullname': 'Jean Dupont',
            'email': 'invalid_email',  # Email invalide
            'phone': '0612345678',
            'password': 'password123',
            'confirmPassword': 'password123'
        }
        form = CitoyenForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("Enter a valid email address.", form.errors['email'])

    def test_password_mismatch(self):
        form_data = {
            'fullname': 'Jean Dupont',
            'email': 'jean.dupont@example.com',
            'phone': '0612345678',
            'password': 'password123',
            'confirmPassword': 'password456'  # Mots de passe différents
        }
        form = CitoyenForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("Les mots de passe ne correspondent pas.", form.errors['__all__'])

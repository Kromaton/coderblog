from django.test import TestCase
from profiles.forms import UserRegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm


class ProfileTests(TestCase):

    def test_registro(self):
        formulario = User(last_name="Nombre", first_name="Apellido", username="test", email="email@gmail.com", password="testoprueba")
        formulario.save()
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(formulario.last_name, "Nombre")
        self.assertEqual(formulario.first_name, "Apellido")
        self.assertEqual(formulario.username, "test")
        self.assertEqual(formulario.email, "email@gmail.com")
        self.assertEqual(formulario.password, "testoprueba")
        
    def test_login_view(self):
        user = User(last_name="Nombre", first_name="Apellido", username="test", email="email@gmail.com", password="testoprueba")
        user.save()
        usuario = "test"
        password = "testoprueba"
        user = authenticate(username=usuario, password=password)

    


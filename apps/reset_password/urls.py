from django.urls import path
from django.contrib.auth.tokens import PasswordResetTokenGenerator

from . import views

urlpatterns = [
        path("", views.index, name="reset-password"),
        path("",
        ]


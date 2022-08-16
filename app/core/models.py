from django.db import models

# Create your models here.

class LoginForm(models.Model):
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username

    class Meta:
        app_label = 'login_form'
    
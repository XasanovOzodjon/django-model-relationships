from django.db import models


class User(models.Model):
    username = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.username


class UserSettings(models.Model):
    LAN_CHOICES = [
        ['en', 'English'],
        ['uz', 'Uzbek'],
        ['ru', 'Russian'],
    ]
    MODE_CHOICES = [
        ['dark', 'Dark'],
        ['light', 'Light'],
    ]
    lang = models.CharField(max_length=10, choices=LAN_CHOICES, default='en')
    mode = models.CharField(max_length=10, choices=MODE_CHOICES, default='light')
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, related_name='settings')

    def __str__(self):
        return self.user.username
    
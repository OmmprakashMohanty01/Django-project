from django.db import models

class Profile(models.Model):
    telegram_username = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.telegram_username

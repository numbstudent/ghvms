from django.db import models

# Create your models here.


class Disclaimer(models.Model):
    disclaimertext = models.TextField()

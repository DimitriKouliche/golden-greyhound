from django.db import models

class Enigma(models.Model):
    expected_answer = models.CharField(max_length=200)
    secret_key = models.CharField(max_length=200)
    next_key = models.CharField(max_length=200)
    template_name = models.CharField(max_length=200)

class Contestant(models.Model):
    name = models.CharField(max_length=200)
    date_finished = models.DateTimeField(auto_now=True)
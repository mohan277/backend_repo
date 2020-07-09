from django.db import models

# Write a Snippet model in models.py with title and code as TextFields.

class Snippet(models.Model):
    title = models.TextField()
    code = models.TextField()
from django.db import models


class Category(models.Model):
    name = models.TextField()
    description = models.TextField()

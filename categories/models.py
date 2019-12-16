from django.db import models


class Category(models.Model):
    name = models.TextField()
    description = models.TextField()


class SubCategory(models.Model):
    name = models.TextField()
    description = models.TextField()
    category = models.ForeignKey("Category", on_delete=models.CASCADE)

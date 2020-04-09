from django.db import models


class Category(models.Model):
    name = models.TextField()
    description = models.TextField(null=True)

    @staticmethod
    def from_post_data(post_data) -> "Category":
        category = Category()
        category.id = post_data.get("id")
        category.name = post_data.get("name")
        category.description = post_data.get("description")
        return category


class SubCategory(models.Model):
    name = models.TextField()
    description = models.TextField(null=True)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)

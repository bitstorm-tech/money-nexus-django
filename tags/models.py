from django.db import models
from django.http import QueryDict


class Tag(models.Model):
    name = models.TextField(unique=True)
    description = models.TextField(null=True)

    @staticmethod
    def from_post_data(post_data: QueryDict) -> "Tag":
        tag = Tag()
        if "id" in post_data:
            tag.id = post_data["id"]
        tag.name = post_data.get("name", "")
        tag.description = post_data.get("description", "")
        return tag

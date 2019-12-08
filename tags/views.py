from django.http import HttpRequest
from django.shortcuts import render

from categories.models import Category
from tags.models import Tag


def tags(request: HttpRequest):
    all_tags = Tag.objects.all().order_by("name")
    all_categories = Category.objects.all().order_by("name")
    context = {"tags": all_tags, "categories": all_categories, "active": "tags"}

    if request.method == "POST":
        save_tag(request.POST)
    elif request.method == "GET":
        context["name"] = request.GET.get("name", "")
        context["description"] = request.GET.get("description", "")

    return render(request, "tags/tags.html", context)


def save_tag(post_data):
    name = post_data["name"]
    description = post_data["description"]
    category_id = post_data["category"]
    tag = Tag(name=name, description=description, category_id=category_id)
    tag.save()

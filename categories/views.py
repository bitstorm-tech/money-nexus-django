from django.http import HttpRequest
from django.shortcuts import render

from categories.models import Category


def categories(request: HttpRequest):
    context = {"active": "categories"}

    if request.method == "POST":
        save_category(request.POST)
    else:
        all_categories = list(Category.objects.order_by("name").values())
        context["categories"] = all_categories

    return render(request, "categories/categories.html", context)


def save_category(post_data):
    category = Category()
    category.name = post_data["name"]
    category.description = post_data["description"]
    category.save()

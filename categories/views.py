from django.http import HttpRequest
from django.shortcuts import render

from categories.models import Category


def categories(request: HttpRequest):
    if request.method == "POST":
        save_category(request.POST)

    return render(request, "categories/categories.html")


def save_category(post_data):
    category = Category()
    category.name = post_data["name"]
    category.description = post_data["description"]
    category.save()

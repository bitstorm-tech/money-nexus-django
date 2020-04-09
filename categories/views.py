from django.http import HttpRequest
from django.shortcuts import render

from categories.models import Category


def categories(request: HttpRequest):
    context = {"active": "categories"}

    if request.method == "POST":
        Category.from_post_data(request.POST).save()
    else:
        all_categories = list(Category.objects.order_by("name").values())
        context["categories"] = all_categories

    return render(request, "categories/categories.html", context)

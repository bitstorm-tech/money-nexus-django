from django.http import HttpRequest
from django.shortcuts import render

from money_planner_app.models.tag import Tag


def tags(request: HttpRequest):
    all_tags = Tag.objects.all().order_by("name")
    context = {"tags": all_tags}

    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        tag = Tag(name=name, description=description)
        tag.save()
    elif request.method == "GET":
        context["name"] = request.GET.get("name", "")
        context["description"] = request.GET.get("description", "")

    return render(request, "money_planner_app/tags.html", context)

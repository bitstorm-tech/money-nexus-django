import datetime

from django.http import HttpRequest
from django.shortcuts import render

from money_planner_app.models import Tag


def transactions(request: HttpRequest):
    all_tags = Tag.objects.all()
    context = {"now": datetime.date.today().strftime("%Y-%m-%d"), "tags": all_tags}

    return render(request, "money_planner_app/transactions.html", context)


def tags(request: HttpRequest):
    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        tag = Tag(name=name, description=description)
        tag.save()

    all_tags = Tag.objects.all()
    context = {"tags": all_tags}
    return render(request, "money_planner_app/tags.html", context)

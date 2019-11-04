import datetime

from django.http import HttpRequest
from django.shortcuts import render

from money_planner_app.models.tag import Tag


def transactions(request: HttpRequest):
    all_tags = Tag.objects.all().order_by("name")
    context = {"now": datetime.date.today().strftime("%Y-%m-%d"), "tags": all_tags}

    return render(request, "money_planner_app/transactions.html", context)

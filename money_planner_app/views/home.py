from django.http import HttpRequest
from django.shortcuts import render


def home(request: HttpRequest):
    return render(request, "money_planner_app/home.html")

from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.views import View

from money_nexus.json_utils import to_json
from tags.models import Tag


class TagsView(View):
    def get(self, request: HttpRequest):
        tags = Tag.objects.all().order_by("name")
        context = {"tags": to_json(tags), "active": "tags"}
        return render(request, "tags/tags.html", context)

    def post(self, request: HttpRequest):
        tag = Tag.from_post_data(request.POST)
        if tag.id:
            Tag.objects.filter(id=tag.id).update(
                name=tag.name, description=tag.description
            )
        else:
            tag.save()
        return redirect("/tags")


def delete_tag(request: HttpRequest):
    Tag.objects.filter(request.POST["id"]).delete()
    return redirect("/tags")

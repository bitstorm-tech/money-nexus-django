from django.urls import path

from tags.views import TagsView, delete_tag

urlpatterns = [
    path("", TagsView.as_view(), name="tags"),
    path("delete", delete_tag, name="tags_delete"),
]

import json

from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import QuerySet


def to_json(model: QuerySet) -> str:
    python_object_list = serializers.serialize("python", model)
    result = []
    for python_object in python_object_list:
        result.append({"id": python_object["pk"], **python_object["fields"]})
    return json.dumps(result, cls=DjangoJSONEncoder)

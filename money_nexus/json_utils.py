import json

from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import QuerySet


def to_json(model: QuerySet) -> str:
    return json.dumps(list(model.values()), cls=DjangoJSONEncoder)

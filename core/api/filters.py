from django.db.models.functions import Lower
from django_filters import OrderingFilter


class LowerOrderingFilter(OrderingFilter):
    def __init__(self, *args, **kwargs):
        self.text_fields = kwargs.pop("text_fields", tuple())
        super().__init__(*args, **kwargs)

    def get_ordering_value(self, param):
        descending = param.startswith("-")
        _param = param[1:] if descending else param
        ordering_value = super().get_ordering_value(param)
        if _param in self.text_fields:
            return Lower(_param).desc() if descending else Lower(_param)
        return ordering_value


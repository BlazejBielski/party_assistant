from django.forms import ModelForm
from . import models

from django.utils.translation import gettext_lazy as _


class SoupForm(ModelForm):
    class Meta:
        model = models.Soup
        fields = ["name", "description", "price", "image", "is_vegetarian", "is_gluten_free", "is_low_carb", "is_keto"]
        labels = {
            "name": _("Name"),
            "description": _("Description"),
            "price": _("Price"),
        }
        help_texts = {"is_vegetarian": _("Is soup is vegetarian?")}

        error_messages = {
            "name": {
                "max_length": _("Name is too long."),
                "unique": _("Name is not unique"),
            }
        }


form = SoupForm()

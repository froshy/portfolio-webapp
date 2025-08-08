from django.db import models
from django.utils.translation import gettext_lazy as _

class CategoryChoices(models.TextChoices):
    tech = "tech", _("Tech")
    personal = "personal", _("Personal")
    shower_thoughts = "shower thoughts", _("Shower Thoughts")
    general = "general", _("General")

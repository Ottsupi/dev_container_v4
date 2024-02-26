import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _


class HelloMessages(models.Model):
    uuid = models.UUIDField(
        default=uuid.uuid4,
        editable=False
    )

    message = models.CharField(max_length=255)

    class Carrier(models.TextChoices):
        DJANGO = 'DJG', _('Django')
        DRF = 'DRF', _('Django Rest Framework')

    carrier = models.CharField(
        max_length=3,
        choices=Carrier.choices,
        default=Carrier.DJANGO,
    )

    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.message

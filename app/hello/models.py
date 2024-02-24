from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


# Create your models here.
class HelloMessage(models.Model):
    '''
    Sample model
    '''
    message_body = models.CharField(max_length = 255)
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Carriers(models.TextChoices):
        DJANGO = 'DGJ', _('Django')
        DRF = 'DRF', _('Django Rest Framework')

    carrier = models.CharField(
        max_length=3,
        choices=Carriers.choices,
        default=Carriers.DJANGO
    )
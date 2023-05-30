import uuid

from django_extensions.db.models import TimeStampedModel, ActivatorModel, TitleDescriptionModel

from django.db import models


class Product(TimeStampedModel, ActivatorModel, TitleDescriptionModel, models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    price = models.DecimalField(null=False, decimal_places=2, max_digits=12)


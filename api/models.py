from django.db import models
from uuid import uuid4
import jsonfield
import collections

class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4(), editable=False, auto_created=True)
    data = jsonfield.JSONField(blank=True, null=True, load_kwargs={'object_pairs_hook': collections.OrderedDict})

class Organization(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4(), editable=False, auto_created=True)
    data = jsonfield.JSONField(blank=True, null=True, load_kwargs={'object_pairs_hook': collections.OrderedDict})

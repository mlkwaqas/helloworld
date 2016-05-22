from __future__ import unicode_literals

from django.db import models


class Name(models.Model):
    value = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

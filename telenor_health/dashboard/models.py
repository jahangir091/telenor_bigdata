# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.



from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class FactTable(models.Model):
    title = models.CharField(max_length=300)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

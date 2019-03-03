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


class Fact(models.Model):
    membership_no = models.CharField(max_length=300, null=True, blank=True)
    first_free_join_date = models.DateTimeField(null=True, blank=True)
    last_free_subscription_date = models.DateTimeField(null=True, blank=True)
    first_piad_subscription_date = models.DateTimeField(null=True, blank=True)
    last_piad_subscription_date = models.DateTimeField(null=True, blank=True)
    number_of_renew_performed = models.IntegerField(blank=True, null=True)
    number_of_paid_subscription = models.IntegerField(blank=True, null=True)
    first_retailer_or_channel = models.CharField(max_length=300, null=True, blank=True)
    avg_membership_duration = models.FloatField(blank=True, null=True)

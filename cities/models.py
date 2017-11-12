# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.core.validators import MaxValueValidator

class City(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, blank=False)
    country_code = models.CharField(max_length=3, blank=True, db_column='CountryCode')
    district = models.CharField(max_length=30)
    population = models.IntegerField(validators=[MaxValueValidator(20)])

    class Meta:
        managed = False
        db_table = 'city'

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from countries.models import Country

class CountryLanguage(models.Model):
    OFFICIAL_CHOICES = (
            ('T', 'True'),
            ('F', 'False'),
    )
    country_code = models.ForeignKey(Country, db_column='CountryCode')
    language = models.CharField(max_length=20,primary_key=True)
    is_official = models.CharField(max_length=1, choices=OFFICIAL_CHOICES, db_column='IsOfficial')
    percentage = models.DecimalField(max_digits=2, decimal_places=1)

    class Meta:
        managed = False
        db_table = 'countrylanguage'

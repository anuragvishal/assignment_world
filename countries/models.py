# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.core.validators import MaxValueValidator

class Country(models.Model):
    code = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, blank=True)
    continent = models.CharField(max_length=30)
    region = models.CharField(max_length=60)
    surface_area = models.DecimalField(max_digits=20, decimal_places=4, db_column='SurfaceArea')
    indep_year = models.IntegerField(validators=[MaxValueValidator(4)], null=True, db_column='IndepYear')
    population = models.IntegerField(validators=[MaxValueValidator(30)])
    life_expectancy = models.DecimalField(max_digits=2, decimal_places=1, null=True, db_column='LifeExpectancy')
    gnp = models.DecimalField(max_digits=10, decimal_places=2)
    gnp_old = models.DecimalField(max_digits=10, decimal_places=2, null=True, db_column='GNPOld')
    local_name = models.CharField(max_length=20, null=True, db_column='LocalName')
    government_form = models.CharField(max_length=40, db_column='GovernmentForm')
    head_of_state = models.CharField(max_length=50, db_column='HeadOfState')
    capital = models.IntegerField(validators=[MaxValueValidator(6)], null=True)
    code_2 = models.CharField(max_length=2, db_column='Code2')

    class Meta:
        managed = False
        db_table = 'country'

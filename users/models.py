# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models




class Users(models.Model):
    GENDER_CHOICES = (
            ('M', 'Male'),
            ('F', 'Female'),
    )
    id = models.IntegerField()
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=False)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    email_id = models.EmailField(primary_key=True, max_length=100, unique=True,)
    phone_number = models.CharField(max_length=30, blank=False)

    class Meta:
        managed = False
        db_table = 'users'

    def __unicode__(self):
        return self.email_id

from rest_framework import serializers

from .models import CountryLanguage

class CountryLanguageSerializer(serializers.ModelSerializer):

    class Meta:
        model = CountryLanguage
        fields = ('country_code', 'language', 'is_official', 'percentage')

from rest_framework import serializers

from .models import Country

class CountrySerializer(serializers.ModelSerializer):

    class Meta:
        model = Country
        fields = ('code', 'name', 'continent', 'region', 'surface_area', 'indep_year', 'population', 'life_expectancy', 'gnp', 'gnp_old', 'local_name', 'government_form', 'head_of_state')

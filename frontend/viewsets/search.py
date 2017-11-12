from django.shortcuts import render
from rest_framework import viewsets
from cities.models import City
from cities.serializers import CitySerializer
from countries.models import Country
from countries.serializers import CountrySerializer
from countrylanguage.models import CountryLanguage
from countrylanguage.serializers import CountryLanguageSerializer
from rest_framework.response import Response

class SearchView(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

    def list(self, request):
        return Response({
                'success': True,
                'message': 'message Info',
                'data': 'got search'
            })


class ResultsView(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

    def list(self, request):
        return Response({
                'success': True,
                'message': 'message Info',
                'data': 'got ResultsView'
            })

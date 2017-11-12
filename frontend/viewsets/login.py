from django.shortcuts import render
from rest_framework.response import Response

from rest_framework import viewsets
from users.models import Users
from users.serializers import UsersSerializer

class LoginView(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

    def list(self, request):
        return Response({
                'success': True,
                'message': 'message Info',
                'data': 'got LoginView'
            })


class OtpView(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

    def list(self, request):
        return Response({
                'success': True,
                'message': 'message Info',
                'data': 'got OtpView'
            })


class LogoutView(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

    def list(self, request):
        return Response({
                'success': True,
                'message': 'message Info',
                'data': 'got LogoutView'
            })

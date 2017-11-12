from django.shortcuts import render
from rest_framework import viewsets
from users.models import Users
from users.serializers import UsersSerializer
from rest_framework.response import Response

class SignupView(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

    def create(self, request):
        data = request.data
        queryset = Users.objects.all()
        data['id'] = queryset.count() + 1
        print data
        instance = UsersSerializer(data=data)
        if instance.is_valid():
            print 'data valid'
            instance.save
        else:
            print 'data Invalid'
            instance.errors
        return Response({
                'success': True,
                'message': 'Clinics Info',
                'data': instance.data
            })


    def retrieve(self, request, pk=None):
        queryset = Users.objects.get(id=pk)
        user = self.serializer_class(queryset).data
        return Response({
                'success': True,
                'message': 'Clinics Info',
                'data': user
            })

from rest_framework import serializers

from .models import Users

class UsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Users
        fields = ('id', 'first_name', 'last_name', 'gender', 'email_id', 'phone_number')

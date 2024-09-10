from rest_framework import serializers
from .models import SmsProvider , Smstosend

class provider(serializers.ModelSerializer):
    class Meta :
        model=SmsProvider
        fields='__all__'

class Tosend(serializers.ModelSerializer):
    class Meta :
        model=Smstosend
        fields='__all__'
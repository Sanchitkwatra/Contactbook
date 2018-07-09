from rest_framework import serializers

from . import models

class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        fields='__all__'
        model=models.Contact
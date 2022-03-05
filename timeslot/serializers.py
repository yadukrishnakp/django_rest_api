from rest_framework import serializers
from . import models


class RegisterSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Register
        fields = '__all__'

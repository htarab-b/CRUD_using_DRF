from rest_framework import serializers
from rest_framework.validators import ValidationError
from .models import *

class NameListSerializer(serializers.ModelSerializer):
    class Meta:
        model = NameList
        fields = '__all__'
    def validate(self, data):
        if len(data['phone']) != 10:
            raise ValidationError("Phone number must be only 10 numbers long")
        if not (str(data['phone']).isdigit()):
            raise ValidationError("Phone numbers should contain only numerical values")
        if data['age'] < 1:
            raise ValidationError("Age should be a positive integer")
        return super().validate(data)
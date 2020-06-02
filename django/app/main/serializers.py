from rest_framework import serializers
from main.models import locData

class LocDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = locData
        fields = ('locstate','locdistrict','locemail',)      

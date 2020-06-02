from rest_framework import serializers
from main.models import clgData,locData

class ClgDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = clgData
        fields = ('cname',)
class LocDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = locData
        fields = ('locstate','locdistrict','locemail',)      

from rest_framework import serializers
from main.models import clgData

class ClgDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = clgData
        fields = ('cname',)      

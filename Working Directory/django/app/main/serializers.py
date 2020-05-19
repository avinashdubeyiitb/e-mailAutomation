from rest_framework import serializers
from main.models import clgData,tempCollegeData

class ClgDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = clgData
        fields = ('cname',)


class TempSerializer(serializers.ModelSerializer):

    class Meta:
        model = tempCollegeData
        fields = (
        'remail',
        'ccbcc',
        'name',
        'designation',
        'department',
        'cname',
        'cno')
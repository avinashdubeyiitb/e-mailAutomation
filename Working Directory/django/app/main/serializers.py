from rest_framework import serializers
from main.models import clgData,editMail

class ClgDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = clgData
        fields = ('cname',)

class EditMailSerializer(serializers.ModelSerializer):

    class Meta:
        model = editMail
        fields = ('to','ccbcc','subject','body','attachments',)        

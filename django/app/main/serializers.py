from rest_framework import serializers
from main.models import create_workshop,WorkshopTeamStatus

class CreateWorkshop(serializers.ModelSerializer):

    class Meta:
        model = create_workshop
        fields = (
        'hcn',
        'startdate',
        'enddate',
        'venueadd',
        'cooname',
        'cooemail',
        'coono',)

class WorkshopTeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = WorkshopTeamStatus
        fields = (
            'workshop_venue',
            'date',
            'district',
            'responder',
        )        

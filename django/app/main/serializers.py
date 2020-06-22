from rest_framework import serializers
from main.models import create_workshop,WorkshopTeamStatus,ssn_detail

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
            'workshop_id',
            'workshop_venue',
            'date',
            'district',
            'responder',
        )
# class UserSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = User
#         fields = ('username', 'email', 'first_name', 'last_name', 'photo')
#         read_only_fields = ('email', )

class SsnSerializer(serializers.ModelSerializer):

    class Meta:
        model = ssn_detail
        fields = ('ssn_id','user','timestamp','mail_label','rcptmailid','delegated_access','dcprovider')

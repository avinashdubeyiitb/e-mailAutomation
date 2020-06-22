from rest_framework import serializers
<<<<<<< HEAD
from main.models import create_workshop,WorkshopTeamStatus
=======
from main.models import create_workshop,WorkshopTeamStatus,User,ssn_detail
>>>>>>> 08c9326da907b570b272d625ff6d6a6d73035111

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
<<<<<<< HEAD
# class UserSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = User
#         fields = ('username', 'email', 'first_name', 'last_name', 'photo')
#         read_only_fields = ('email', )
=======
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'photo')
        read_only_fields = ('email', )

class SsnSerializer(serializers.ModelSerializer):

    class Meta:
        model = ssn_detail
        fields = ('ssn_id','user','timestamp','mail_label','rcptmailid','delegated_access','dcprovider')
>>>>>>> 08c9326da907b570b272d625ff6d6a6d73035111

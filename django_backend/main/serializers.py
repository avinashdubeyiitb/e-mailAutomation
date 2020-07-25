from rest_framework import serializers
from main.models import create_workshop,WorkshopTeamStatus,User,ssn_detail,algo_detail,app_normalised_name

class NormalizedSerializer(serializers.ModelSerializer):
    class Meta:
        model = app_normalised_name
        fields = (
            'college_name',
            'normalised_ins_name',
        )

class AlgoDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = algo_detail
        fields = (
        'demo_module_cnt',
    'will_ttl_wrkshp_cnt',
    'aval_ttl_wrkshp_cnt',
    'willcriteria',
    'availcriteria')

class CreateWorkshop(serializers.ModelSerializer):

    class Meta:
        model = create_workshop
        fields = (
        'clgid',
        'hcn',
        'startdate',
        'enddate',
        'venueadd',
        'cooname',
        'cooemail',
        'coono',
        'isactive',)

class WorkshopTeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = WorkshopTeamStatus
        fields = (
            'workshop_id',
            'workshop_venue',
            'district',
            'date',
            'responder',
        )
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'photo')
        read_only_fields = ('email', )

class SsnSerializer(serializers.ModelSerializer):

    class Meta:
        model = ssn_detail
        fields = ('ssn_id','user','timestamp','mail_label','rcptmailid','delegated_access','dcprovider','messageid')

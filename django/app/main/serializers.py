from rest_framework import serializers
from main.models import create_workshop

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

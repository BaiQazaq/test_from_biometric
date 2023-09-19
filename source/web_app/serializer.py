from rest_framework import serializers
from web_app.models import People

class PeopleSerializer(serializers.ModelSerializer):

    class Meta:
        model = People
        fields = ('name', 'inn', 'age', 'created_at', 'changed_at')
        read_only_fields = ('id', 'created_at', 'changed_at')

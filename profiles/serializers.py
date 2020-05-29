from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ('url', 'id', 'profile_code', 'last_name', 'first_name', 'middle_name', 'birth_date', 'gender', 'home_address')
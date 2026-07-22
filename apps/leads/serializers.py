from rest_framework import serializers
from .models import Lead


class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = [
            'id', 'name', 'mobile', 'city', 'interested_model',
            'preferred_contact_time', 'message', 'source',
            'status', 'created_at',
        ]
        read_only_fields = ['id', 'status', 'created_at']
        extra_kwargs = {
            'preferred_contact_time': {'required': False, 'allow_blank': True},
            'message': {'required': False, 'allow_blank': True},
            'source': {'required': False},
        }

    def validate_mobile(self, value):
        value = value.strip()
        if not value.isdigit() or len(value) != 10:
            raise serializers.ValidationError('Enter a valid 10-digit mobile number.')
        return value

    def validate_name(self, value):
        value = value.strip()
        if len(value) < 2:
            raise serializers.ValidationError('Enter your full name.')
        return value
from rest_framework import serializers

from .models import HelloMessages


class HelloMessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = HelloMessages
        fields = ['uuid', 'message', 'carrier', 'date_created', 'last_modified']

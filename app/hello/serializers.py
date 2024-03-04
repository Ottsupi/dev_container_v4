import pytz
from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import HelloMessages


class HelloMessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = HelloMessages
        fields = ('message', 'carrier', 'date_created', 'last_modified')


class HelloReadSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()

    class Meta:
        model = HelloMessages
        fields = ('message', 'carrier', 'date_created', 'last_modified', 'url')

    def get_url(self, obj):
        request = self.context.get('request')
        return reverse('hello-detail', kwargs={'id': obj.id}, request=request)

    def to_representation(self, instance: HelloMessages):
        data = super().to_representation(instance)

        # Convert UTC to Japan time
        tokyo = pytz.timezone('Asia/Tokyo')
        display_format = '%Y-%m-%d %H:%M:%S %Z'
        data['date_created'] = instance.date_created.astimezone(tokyo).strftime(display_format)
        data['last_modified'] = instance.last_modified.astimezone(tokyo).strftime(display_format)

        # Display human-readable name
        data['carrier'] = instance.get_carrier_display()

        return data


class HelloWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = HelloMessages
        fields = ('message', 'carrier')


class HelloReadViewSetSerializer(HelloReadSerializer):
    def get_url(self, obj: HelloMessages):
        request = self.context.get('request')
        return reverse('hellomessages-detail', kwargs={'id': obj.id}, request=request)

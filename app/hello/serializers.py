from datetime import datetime

from pytz import timezone
from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import HelloMessage


class HelloReadSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only = True)

    class Meta:
        model = HelloMessage
        fields = ['id', 'message_body', 'date_created', 'last_modified', 'carrier', 'url']

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        TZ_TOKYO = timezone('Asia/Tokyo')
        FORMAT = '%Y-%m-%d %H:%M:%S %Z'

        date_created: datetime = instance.date_created
        representation['date_created'] = date_created.astimezone(TZ_TOKYO).strftime(FORMAT)

        last_modified: datetime = instance.last_modified
        representation['last_modified'] = last_modified.astimezone(TZ_TOKYO).strftime(FORMAT)

        representation['carrier'] = instance.get_carrier_display()

        return representation

    def get_url(self, obj):
        request = self.context.get('request')
        if request is None: return None
        return reverse('hellomessage-detail', kwargs={'id': obj.id}, request=request)


class HelloWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = HelloMessage
        fields = ['message_body', 'carrier']


# TODO: Write a serializer to for the ViewSets
#       Current: returns {url}/hello/1/detail"
#       Expected: returns {url}/message/1
#
# Possible solution:
#   https://stackoverflow.com/questions/56050182/how-to-reverse-a-url-that-is-using-defaultrouter

from rest_framework import serializers
from .models import OPAStatus, OPAStatusLabel, OPAStatusBundle, OPALog
import logging

logger = logging.getLogger(__name__)

class LabelSerializer(serializers.Serializer):
    """
    {
        'app': 'myapp',
        'environment': 'production',
        'id': 'b1f0bcc2-e00b-429f-b9e9-c568f2f2d448',
        'region': 'west',
        'version': '0.12.0'
    }
    """
    class Meta:
        model = OPAStatusLabel
        field = ['__all__',]
    # app = serializers.CharField(max_length=1024)


class BundleSerializer(serializers.Serializer):
    class Meta:
        model = OPAStatusBundle
        field = ['__all__',]


class OPAStatusSerializer(serializers.Serializer):
    """
    {
        'labels': {
            'app': 'myapp',
            'environment': 'production',
            'id': 'b1f0bcc2-e00b-429f-b9e9-c568f2f2d448',
            'region': 'west',
            'version': '0.12.0'
        },
        'bundle': {
            'name': 'http-example',
            'last_successful_activation': '0001-01-01T00:00:00Z',
            'last_successful_download': '0001-01-01T00:00:00Z',
            'code': 'bundle_error',
            'message': 'server replied with HTTP 500'
            }
    }
    """

    labels = LabelSerializer()
    bundle = BundleSerializer(required=False)


class OPALogsSerializer(serializers.ModelSerializer):
    """
    """
    class Meta:
        model = OPALog

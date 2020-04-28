from django.db import models

class OPAStatusLabel(models.Model):
    app = models.CharField(max_length=256)
    environment = models.CharField(max_length=256)
    uuid = models.CharField(max_length=256)
    region = models.CharField(max_length=256)
    version = models.CharField(max_length=256)


class OPAStatusBundle(models.Model):
    name = models.CharField(max_length=256)
    last_successful_activation = models.CharField(max_length=256)
    last_successful_download = models.CharField(max_length=256)
    code = models.CharField(max_length=256)
    message = models.CharField(max_length=256)


class OPAStatusPlugins(models.Model):
    """
    "plugins": {
        "bundle": {
          "state": "OK"
        },
        "decision_logs": {
          "state": "OK"
        },
        "discovery": {
          "state": "OK"
        },
        "status": {
          "state": "OK"
        }
    }
    """

class OPAStatus(models.Model):
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
    labels = models.ForeignKey('opa.OPAStatusLabel', on_delete=models.CASCADE)
    bundle = models.ForeignKey('opa.OPAStatusBundle', on_delete=models.CASCADE)

class OPALog(models.Model):
    entry = models.CharField(max_length=1024)

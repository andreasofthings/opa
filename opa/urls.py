"""
urly.py.

Route requests from OPA Agent.

"""

import logging
from django.urls import path, include
from .views import OPAStatus, OPABundle, OPALogs

logger = logging.getLogger(__name__)

app_name = 'opa'


urlpatterns = [
    path(r"v1/bundles/<slug:bundle>", OPABundle.as_view()),
    path(r"v1/status", OPAStatus.as_view()),
    path(r"v1/logs", OPALogs.as_view()),
]

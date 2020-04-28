import io
import tarfile
import logging
from contextlib import closing

from django.http import HttpResponse
from django.contrib.auth import get_user_model

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions

from .serializers import OPAStatusSerializer, OPALogsSerializer

import logging

logger = logging.getLogger(__name__)

"""
See:
    https://www.openpolicyagent.org/docs/latest/bundles/
"""


class OPAStatus(APIView):

    queryset = get_user_model().objects.all()
    permission_classes = (permissions.AllowAny,)


    def post(self, request, format=None):
        """POST method."""
        logging.info(
            "Status Bearer Token: %s",
            request.META.get('HTTP_AUTHORIZATION', None)
        )

        serializer = OPAStatusSerializer(data=request.data)

        if serializer.is_valid():
            if 'bundle' in serializer.validated_data:
                logging.info(f"Bundle Name: {serializer.validated_data['bundle']}")

        else:
            logging.error(f"Status De-Serialization failure {serializer.errors}")
            logging.error(request.data)
        return Response("OK!", status=status.HTTP_200_OK)


class OPALogs(APIView):

    queryset = get_user_model().objects.all()
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        """Dump Log."""
        logging.info(
            "Logs Bearer Token: %s",
            request.META.get('HTTP_AUTHORIZATION', None)
        )
        logging.error(f"request.data")
        serializer = OPALogsSerializer(data=request.data)

        return Response("OK!", status=status.HTTP_200_OK)


class OPABundle(APIView):
    # queryset = get_user_model().objects.all()
    permission_classes = (permissions.AllowAny,)

    def get(self, request, bundle=None):
        logging.info(
            "Bundle Bearer Token: %s",
            request.META.get('HTTP_AUTHORIZATION', None)
        )
        bundle = """
        $ tar czvf bundle.tar.gz .
        ./
        ./http/
        ./http/policy.rego
        ./http/data.json
        ./.manifest
        """

        rego = """
        package %s

        default hello = false

        hello {
            input.message == "world"
        }
        """ % "http"

        io_bytes = io.BytesIO()
        tar = tarfile.open(fileobj=io_bytes, mode="w:gz")

        with closing(io.BytesIO(rego.encode())) as f:
            tarf = tarfile.TarInfo(name="http.rego")
            tarf.size = len(f.getvalue())
            tar.addfile(tarf, f)
        tar.close()

        return HttpResponse(
            io_bytes.getvalue(),  # f.read(),
            status=status.HTTP_200_OK,
            content_type="application/gzip"
        )

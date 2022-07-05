import logging
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

logging.basicConfig(level=logging.INFO)


class HealthCheckAPI(APIView):
    permission_classes=(AllowAny,)

    def get(self, request):
        data={
            'message': 'Django Demo Project Health OK',
            'method': str(self.request.method).lower()
        }
        logging.info('ORDER API SERVICE HEALTH IS OKAY')
        return Response(data={'data': data}, status=status.HTTP_200_OK)

    
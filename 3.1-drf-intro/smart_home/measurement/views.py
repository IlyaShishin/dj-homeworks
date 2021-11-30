# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.generics import ListCreateAPIView, CreateAPIView, RetrieveUpdateAPIView, RetrieveAPIView
from rest_framework.response import Response

from .models import Sensor, Measurement
from .serializers import SensorSerializer, SensorDetailSerializer


class SensorCreateAndView(ListCreateAPIView):
    queryset = Sensor.objects.all
    serializer_class = SensorSerializer(queryset, many=True)

    def post(self, request, *args, **kwargs):
        return Response({'status': 'OK'})


class SensorUpdateAndSensorMeasurementView(RetrieveUpdateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = SensorDetailSerializer

    def patch(self, request, *args, **kwargs):
        return Response({'status': 'OK'})


class MeasurementCreate(CreateAPIView):
    def post(self, request, *args, **kwargs):
        return Response({'status': 'OK'})









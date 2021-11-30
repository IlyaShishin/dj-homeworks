from django.urls import path

from measurement.views import SensorCreateAndView, MeasurementCreate, SensorUpdateAndSensorMeasurementView

urlpatterns = [
    path('sensors/', SensorCreateAndView.as_view()),
    path('sensors/<pk>/', SensorUpdateAndSensorMeasurementView.as_view()),
    path('measurements/', MeasurementCreate.as_view()),
]

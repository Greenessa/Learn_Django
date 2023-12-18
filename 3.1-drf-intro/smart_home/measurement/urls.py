from django.urls import path

from measurement.views import SensorUpdate, SensorList, MeasurementCreate, sensor_index

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('', sensor_index),
    path('sensors/', SensorList.as_view(), name='sensors'),
    path('sensors/<int:pk>/', SensorUpdate.as_view()),
    path('measurements/', MeasurementCreate.as_view()),
]

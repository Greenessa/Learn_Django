from django.contrib import admin

from measurement.models import Sensor, Measurement


# Register your models here.
@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
	list_display = ('name', 'description',)
	list_filter = ('name',)


@admin.register(Measurement)
class MeasurementAdmin(admin.ModelAdmin):
	readonly_fields = ('created_at',)
	list_display = ('sensor', 'temperature', 'created_at',)
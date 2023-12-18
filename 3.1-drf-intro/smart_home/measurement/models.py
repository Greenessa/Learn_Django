from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)


class Sensor(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    class Meta:
        verbose_name = 'Датчик'
        verbose_name_plural = 'Датчики'
    def __str__(self):
        return self.name

class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = 'Измерение'
        verbose_name_plural = 'Показания'
        ordering = ['-created_at']

    def __str__(self):
        return f"Измерение для {self.sensor.name} в {self.created_at}: {self.temperature}."
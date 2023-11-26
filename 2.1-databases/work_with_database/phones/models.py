from django.db import models
from django.utils.text import slugify


class Phone(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="Номер id")
    name = models.CharField(max_length=100, verbose_name="Название")
    price = models.FloatField(verbose_name="Цена")
    image = models.ImageField(verbose_name="Изображение")
    release_date = models.DateField(verbose_name="Дата выпуска")
    lte_exists = models.BooleanField(verbose_name="LTE")
    slug = models.SlugField(unique=True, verbose_name="URL")
    #slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return f'{self.name}, {self.price}: {self.release_date}'

    def save(self, **kwargs):
        super(Phone, self).save()
        if not self.slug:
            self.slug = slugify(self.name)
            super(Phone, self).save(**kwargs)
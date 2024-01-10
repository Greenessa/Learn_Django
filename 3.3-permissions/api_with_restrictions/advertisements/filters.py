#from django_filters import rest_framework as filters, DateTimeFromToRangeFilter
import django_filters
from django_filters import DateTimeFromToRangeFilter

from advertisements.models import Advertisement


class AdvertisementFilter(django_filters.FilterSet):
    """Фильтры для объявлений."""
    created_at = DateTimeFromToRangeFilter()
    # TODO: задайте требуемые фильтры

    class Meta:
        model = Advertisement
        fields = ['status', 'creator__username', 'created_at',]


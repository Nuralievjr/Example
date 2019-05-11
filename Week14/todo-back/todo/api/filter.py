from django_filters import rest_framework as filters
from api.models import TaskList


class TaskListFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='exact')

    class Meta:
        model = TaskList
        fields = ('name',)
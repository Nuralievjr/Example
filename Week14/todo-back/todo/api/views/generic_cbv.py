from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from api.models import TaskList, Task
from api.serializers import TaskListSerializerModel, TaskSerializer
from rest_framework.decorators import api_view
from rest_framework import filters
from api.filter import TaskListFilter


class TaskListt(generics.ListCreateAPIView):
    # queryset = Category.objects.all()
    # serializer_class = CategorySerializer2
    permission_classes = (IsAuthenticated, )
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerializerModel
    filter_backends = (DjangoFilterBackend,
                       filters.SearchFilter,
                       filters.OrderingFilter)
    # TODO DjangoFilterBackend
    filter_class = TaskListFilter
    # filterset_fields = ('name', 'price')

    # TODO SearchFilter
    search_fields = ('name', 'price', 'count')

    # TODO OrderingFilter
    ordering_fields = ('name',)

    ordering = ('name',)


class TaskListDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerializerModel


class Task(APIView):

    def get(self, request, pk):
        tasklist = TaskList.objects.get(id=pk)
        tasks = tasklist.task_set.all()
        serializer_class = TaskSerializer(tasks, many=True)
        return Response(serializer_class.data)










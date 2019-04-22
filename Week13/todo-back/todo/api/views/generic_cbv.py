from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404

from api.models import TaskList, Task
from api.serializers import TaskListSerializerModel, TaskSerializer


class TaskListt(generics.ListCreateAPIView):
    # queryset = Category.objects.all()
    # serializer_class = CategorySerializer2
    permission_classes = (IsAuthenticated, )
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerializerModel


class TaskListDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerializerModel


class Task(APIView):

    def get(self, request, pk):
        tasklist = TaskList.objects.get(id=pk)
        tasks = tasklist.task_set.all()
        serializer_class = TaskSerializer(tasks, many=True)
        return Response(serializer_class.data)













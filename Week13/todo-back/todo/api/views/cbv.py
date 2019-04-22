from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.models import TaskList, Task
from api.serializers import TaskListSerializer, TaskSerializer, TaskListSerializerModel


class TaskList(APIView):
    def get(self, request):
        tasklists = TaskList.objects.all()
        serializer = TaskListSerializerModel(tasklists, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TaskListSerializerModel(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class TaskDetail(APIView):

    def get_object(self, pk):
        try:
            return TaskList.objects.get(id=pk)
        except TaskList.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        tasklist = self.get_object(pk)
        serializer = TaskListSerializerModel(tasklist)
        return Response(serializer.data)

    def put(self, request, pk):
        tasklist = self.get_object(pk)
        serializer = TaskListSerializerModel(instance=tasklist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):
        tasklist = self.get_object(pk)
        tasklist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
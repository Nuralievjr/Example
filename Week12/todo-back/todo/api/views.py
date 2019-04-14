from typing import List, Any
import json
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from .models import TaskList, Task
from api.serializers import TaskListSerializer, TaskListSerializerModel,TaskSerializer
from django.views.decorators.csrf import csrf_exempt

# Create your views here.x

@csrf_exempt
def task_lists(request):
    if request.method == 'GET':

        tasks = TaskList.objects.all()

        serializer = TaskListSerializer(tasks, many=True)

        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        serializer = TaskListSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)

@csrf_exempt
def task_ls_detail(request, pk):
    try:
        task_list = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    if request.method == 'GET':
        serializer = TaskListSerializer(task_list)
        return JsonResponse(serializer.data, status=200)
    elif request.method == 'PUT':
        data = json.loads(request.body)
        serializer = TaskListSerializer(instance=data, data=data)
        if serializer.is_valid():
            serializer.save()  # update function in serializer class
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors)
    elif request.method == 'DELETE':
        task_list.delete()
        return JsonResponse({}, status=204)

    return JsonResponse(task_list.to_json(), safe=False)


def task(request, pk):
    try:
        tasklist = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    tasks = tasklist.task_set.all()
    #json_tasks = [t.to_json() for t in tasks]
    serializer = TaskSerializer(tasks, many=True)

    return JsonResponse(serializer.data, safe=False)

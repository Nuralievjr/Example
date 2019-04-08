from django.db import models
from django.utils.timezone import now


# Create your models here.


class TaskList(models.Model):
    name = models.CharField(max_length=200)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name
        }


class Task(models.Model):
    _name = models.CharField(max_length=200)
    created_at = models.DateTimeField(default=now)
    due_on = models.DateTimeField(default=now)
    status = models.CharField(max_length=200)
    task_list = models.ForeignKey(TaskList, on_delete=models.CASCADE)

    def to_json(self):
        return {
            'id': self.id,
            'name': self._name,
            'created_at': self.created_at,
            'due_on': self.due_on,
            'status': self.status,
            'TaskList': self.task_list.id
        }

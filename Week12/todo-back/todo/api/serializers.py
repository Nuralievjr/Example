from rest_framework import serializers
from api.models import TaskList


class TaskListSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)

    def create(self, validated_data):
        t_tl = TaskList(**validated_data)
        t_tl.save()

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()


class TaskListSerializerModel(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)

    class Meta:
        model = TaskList
        fields = ('id', 'name',)


class TaskSerializer(serializers.Serializer):
    _name = serializers.CharField()
    created_at = serializers.DateTimeField()
    due_on = serializers.DateTimeField()
    status = serializers.CharField()
    task_list = TaskListSerializer()

from django.contrib.auth.models import User
from rest_framework import serializers
from . models  import Projects, Tasks, Comments


class CommentCreateSerializer(serializers.ModelSerializer):
    """Комментарий"""

    project = serializers.SlugRelatedField(slug_field='title', queryset=Projects.objects.all())
    user = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())

    class Meta:
        model = Comments
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    """Задачи"""

    project = serializers.SlugRelatedField(slug_field='title', queryset=Projects.objects.all())

    class Meta:
        model = Tasks
        fields = '__all__'


class ProjectsSerializer(serializers.ModelSerializer):
    """Все проекты"""
    start = serializers.DateField()
    end = serializers.DateField()
    task = TaskSerializer(many=True, read_only=True)
    comments = CommentCreateSerializer(many=True, read_only=True)
    supervisor = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())
    developers = serializers.SlugRelatedField(slug_field='username', many=True, queryset=User.objects.all())
    title = serializers.CharField()
    description = serializers.CharField()
    status = serializers.BooleanField()

    class Meta:
        model = Projects
        fields = "__all__"

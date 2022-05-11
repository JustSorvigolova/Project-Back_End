from . serializers import ProjectsSerializer, CommentCreateSerializer, TaskSerializer
from . models import Projects, Comments, Tasks
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class ProjectCreate(generics.CreateAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer
    permission_classes = [IsAdminUser]


class ProjectList(generics.ListAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer
    permission_classes = [IsAuthenticated]


class ProjectUpdateRetrieveDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer
    permission_classes = [IsAuthenticated]


class CommentListCreate(generics.ListCreateAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentCreateSerializer
    permission_classes = [IsAuthenticated]


class CommentUpdateRetrieveDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentCreateSerializer
    permission_classes = [IsAuthenticated]


class TasksListCreate(generics.ListCreateAPIView):
    queryset = Tasks.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]


class TaskUpdateRetrieveDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tasks.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

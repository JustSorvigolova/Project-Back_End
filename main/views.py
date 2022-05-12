from .permissions import IsOwnerOrReadOnly
from .serializers import ProjectsSerializer, CommentCreateSerializer, TaskSerializer, TaskProjectSerializer, \
    ProjectCreateSerializer
from . models import Projects, Comments, Tasks
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated


class ProjectCreate(generics.CreateAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectCreateSerializer
    permission_classes = [IsAuthenticated]


class ProjectList(generics.ListAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]


class ProjectUpdateRetrieveDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer
    permission_classes = [IsAuthenticated]


class CommentListCreate(generics.ListCreateAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentCreateSerializer
    permission_classes = [IsAuthenticated, ]


class CommentUpdateRetrieveDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentCreateSerializer
    permission_classes = [IsAuthenticated, ]


class TasksListCreate(generics.ListCreateAPIView):
    queryset = Tasks.objects.all()
    serializer_class = TaskProjectSerializer
    permission_classes = [IsAuthenticated, ]


class TaskUpdateRetrieveDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tasks.objects.all()
    serializer_class = TaskProjectSerializer
    permission_classes = [IsAuthenticated, ]

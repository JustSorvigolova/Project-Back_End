from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path('projectscreate/', views.ProjectCreate.as_view()),
    path('projects/', views.ProjectList.as_view()),
    path('project/<int:pk>/', views.ProjectUpdateRetrieveDelete.as_view()),
    path('comment/', views.CommentListCreate.as_view()),
    path('comment/<int:pk>/', views.CommentUpdateRetrieveDelete.as_view()),
    path('task/', views.TasksListCreate.as_view()),
    path('task/<int:pk>/', views.TaskUpdateRetrieveDelete.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)

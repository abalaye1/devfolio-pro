from django.urls import path
from apps.projects import views



urlpatterns = [
    #path('projects_list/', views.project_list, name='projects'),
    #path("projects/<slug:slug>/", views.project_detail, name="project_detail"),
    path("", views.project_list, name="projects"),
    path("<slug:slug>/", views.project_detail, name="project_detail"),
]

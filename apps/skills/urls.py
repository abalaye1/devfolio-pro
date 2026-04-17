from django.urls import path
from apps.skills import views

urlpatterns = [
    path('',views.skills,name='skills')
    #path("skills/", skills, name="skills"),
]
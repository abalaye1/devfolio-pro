from django.shortcuts import render
from apps.projects.models import Project

# Create your views here.


def home(request):
    featured_projects = (
        Project.objects
        .filter(is_featured=True)
        .prefetch_related("tech_stack")[:3]
    )

    context = {
        "featured_projects": featured_projects,
    }
    return render(request, "home_pages/home.html", context)
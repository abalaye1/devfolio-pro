from django.shortcuts import render , get_object_or_404
from .models import Project, Tech
from django.db.models import Q
from django.core.paginator import Paginator



def project_list(request):
    projects_qs = Project.objects.prefetch_related("tech_stack").all()
    techs = Tech.objects.all()

    selected_tech = request.GET.get("tech")
    query = request.GET.get("q")

    if selected_tech:
        projects_qs = projects_qs.filter(tech_stack__slug=selected_tech)

    if query:
        projects_qs = projects_qs.filter(
            Q(title__icontains=query) |
            Q(short_description__icontains=query) |
            Q(tech_stack__name__icontains=query)
        ).distinct()

    # ✅ PAGINATION — ALWAYS RUNS
    paginator = Paginator(projects_qs, 3)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "projects": page_obj,   # iterable
        "page_obj": page_obj,
        "techs": techs,
        "selected_tech": selected_tech,
        "query": query,
        'projects_qs': projects_qs,
    }

    return render(request, "home_pages/projects.html", context)


def project_detail(request, slug):
    project = get_object_or_404(
        Project.objects.prefetch_related("tech_stack"),
        slug=slug
    )

    # Related projects by shared tech
    related_projects = (
        Project.objects
        .filter(tech_stack__in=project.tech_stack.all())
        .exclude(id=project.id)
        .distinct()
        .prefetch_related("tech_stack")[:3]
    )

    context = {
        "project": project,
        "related_projects": related_projects,
    }

    return render(request, "home_pages/project_detail.html", context)
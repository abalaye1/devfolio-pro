from django.shortcuts import render
from apps.projects.models import Tech


def skills(request):
    techs = (
        Tech.objects
        .prefetch_related("projects", 'blog_posts')
        .order_by("category", "name")
    )

    # Group tech by category
    categories = {}
    for tech in techs:
        categories.setdefault(tech.category, []).append(tech)

    context = {
        "categories": categories,
    }

    return render(request, "home_pages/skills_second.html", context)

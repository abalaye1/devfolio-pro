from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Count, Q, F

from .models import BlogPost


def blog_list(request):
    """
    Blog index page with pagination
    """
    posts_qs = (
        BlogPost.objects
        .filter(is_published=True)
        .order_by("-published_at")
    )

    paginator = Paginator(posts_qs, 3)  # 5 posts per page
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "posts": page_obj,
        "page_obj": page_obj,
    }

    return render(request, "blog/blog_list.html", context)


def blog_detail(request, slug):
    post = get_object_or_404(
        BlogPost.objects.prefetch_related("tech_stack", "tags"),
        slug=slug,
        is_published=True
    )

    # Get current post relations
    tech_ids = post.tech_stack.values_list("id", flat=True)
    tag_ids = post.tags.values_list("id", flat=True)

    # Smart related posts (Tech + Tags weighted scoring)
    related_posts = (
        BlogPost.objects.filter(is_published=True)
        .exclude(id=post.id)
        .annotate(
            shared_tech=Count(
                "tech_stack",
                filter=Q(tech_stack__in=tech_ids)
            ),
            shared_tags=Count(
                "tags",
                filter=Q(tags__in=tag_ids)
            ),
        )
        .annotate(
            score=(F("shared_tech") * 2) + F("shared_tags")
        )
        .filter(score__gt=0)  # only relevant posts
        .order_by("-score", "-published_at")
        .distinct()[:6]
    )

    context = {
        "post": post,
        "related_posts": related_posts,
    }

    return render(request, "blog/blog_detail.html", context)
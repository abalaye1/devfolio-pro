# apps/projects/models.py
from django.db import models



class Tech(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True)
    icon = models.CharField(
        max_length=50,
        blank=True,
        help_text="Bootstrap icon class, e.g. bi bi-database"
    )
    category = models.CharField(
        default="backend",
        max_length=50,
        choices=[
            ("backend", "Backend"),
            ("frontend", "Frontend"),
            ("database", "Database"),
            ("devops", "DevOps"),
            ("tools", "Tools"),
        ]
    )

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    short_description = models.TextField()
    description = models.TextField()
    thumbnail = models.ImageField(upload_to="projects/", blank=True)
    live_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    is_private_repo = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)

    # NEW (case study sections)
    problem = models.TextField(blank=True)
    solution = models.TextField(blank=True)
    challenges = models.TextField(blank=True)
    results = models.TextField(blank=True)

    tech_stack = models.ManyToManyField(
        Tech,
        blank=True,
        related_name="projects"
    )

    def __str__(self):
        return self.title




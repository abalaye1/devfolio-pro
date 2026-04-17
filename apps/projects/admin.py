from django.contrib import admin
from apps.projects.models import Project , Tech


# Register your models here.

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "is_featured")
    prepopulated_fields = {"slug": ("title",)}
    filter_horizontal = ("tech_stack",)


@admin.register(Tech)
class TechAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


from django.db import models

from apps.projects.models import Tech


# Create your models here.




class BlogTag(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    excerpt = models.TextField(blank=True)
    content = models.TextField()
    tags = models.ManyToManyField(
        BlogTag,
        blank=True,
        related_name="posts"
    )
    published_at = models.DateTimeField()
    is_published = models.BooleanField(default=True)

    tech_stack = models.ManyToManyField(
        Tech,
        blank=True,
        related_name="blog_posts"
    )

    def reading_time(self):
        words = len(self.content.split())
        minutes = words // 200  # average reading speed
        return max(1, minutes)

    def __str__(self):
        return self.title






#C) Direct links

#Email

#GitHub

#LinkedIn
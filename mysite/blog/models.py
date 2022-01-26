from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=45, null=False)
    last_name = models.CharField(max_length=45, null=False)
    username = models.CharField(max_length=50, null=False, unique=True)
    password = models.CharField(max_length=32, null=False)
    d_o_b = models.DateField


class Post(models.Model):
    STATUS_CHOICES = (
        ("draft", "Draft"),
        ("published", "Published")
    )

    author = models.ForeignKey(Author, related_name="blog_posts", on_delete=models.CASCADE)

    publish_date = models.DateTimeField()

    title = models.CharField(max_length=45, unique=False)

    slug = models.SlugField(max_length=100, unique_for_date=True)
# Create your models here.

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

    author = models.ForeignKey(Author, on_delete=models.CASCADE)
# Create your models here.

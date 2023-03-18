from django.db import models


# Create your models here.


class Request(models.Model):
    full_name = models.CharField(("Full Name"), max_length=255)
    phone = models.CharField(("Phone"), max_length=25)


class Post(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class PostPhoto(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post_images/')
    caption = models.CharField(max_length=200, blank=True, null=True)


class Project(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class ProjectPhoto(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='useful_images/')
    caption = models.CharField(max_length=200, blank=True, null=True)


class Useful(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=200)
    file = models.FileField(upload_to='useful_files/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class UsefulPhoto(models.Model):
    useful = models.ForeignKey(Useful, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='useful_images/')
    caption = models.CharField(max_length=200, blank=True, null=True)


class Review(models.Model):
    image = models.ImageField(
        upload_to='review_images/')
    created_at = models.DateTimeField(auto_now_add=True)


# CATALOG

class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(
        ("Фото Категории"), upload_to=None, height_field=None, width_field=None, max_length=None, blank=True, null=True)
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    body_material = models.CharField(max_length=100, blank=True, null=True)
    wind_region = models.CharField(max_length=100, blank=True, null=True)
    coating = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(
        ("Image"), upload_to=None, height_field=None, width_field=None, max_length=None, blank=True, null=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='products')

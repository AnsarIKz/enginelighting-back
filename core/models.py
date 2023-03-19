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

    def __str__(self):
        return self.caption


class Project(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class ProjectPhoto(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='project_images/')
    caption = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.caption


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

    def __str__(self):
        return self.caption


class Review(models.Model):
    image = models.ImageField(
        upload_to='review_images/')
    created_at = models.DateTimeField(auto_now_add=True)


# CATALOG

class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(
        ("Фото Категории"), upload_to='category_images/', height_field=None, width_field=None, max_length=None, blank=True, null=True)
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(('Описание'), blank=True, null=True)

    # ADDITIONAL FIELDs
    body_material = models.CharField(
        ('Материал корпуса'), max_length=255, blank=True, null=True)
    wind_region = models.CharField(
        ('Ветровой район'), max_length=255, blank=True, null=True)
    coating = models.CharField(
        ('Покрытие'), max_length=255, blank=True, null=True)
    luminous_flux = models.CharField(
        ("Световой поток, лм"), max_length=255, blank=True, null=True)
    power_consumption = models.CharField(
        ("Потребляемость, вт"), max_length=255, blank=True, null=True)
    operating_voltage = models.CharField(
        ("Рабочее напряжение "), max_length=255, blank=True, null=True)
    plinth_type = models.CharField(
        ("Тип цоколя"), max_length=255, blank=True, null=True)
    led_generation = models.CharField(
        ("Поколение светодиодов"), max_length=50, blank=True, null=True)
    protection_level = models.CharField(
        ("Степень защиты"), max_length=50, blank=True, null=True)
    length = models.CharField(
        ("Длина, мм"), max_length=50, blank=True, null=True)
    size = models.CharField(
        ("Размер, ДxШxВ"), max_length=50, blank=True, null=True)
    height = models.CharField(("Высота"), max_length=50, blank=True, null=True)
    bracket_outreach = models.CharField(
        ("Вылет кронштейна"), max_length=50, blank=True, null=True)
    distance_between_holes = models.CharField(
        ("Расстояние между посадочными отверстиями для закладной, мм"), max_length=50, blank=True, null=True)
    profile_tube_size = models.CharField(
        ("Размер профильной трубы, мм"), max_length=50, blank=True, null=True)
    #
    image = models.ImageField(
        ("Image"), upload_to='product_images/', height_field=None, width_field=None, max_length=None, blank=True, null=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='products', blank=True, null=True)


def __str__(self):
    return self.name

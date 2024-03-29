# Generated by Django 4.1.7 on 2023-03-19 15:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_category_image_alter_product_body_material_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='bracket_outreach',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Вылет кронштейна'),
        ),
        migrations.AddField(
            model_name='product',
            name='distance_between_holes',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Расстояние между посадочными отверстиями для закладной, мм'),
        ),
        migrations.AddField(
            model_name='product',
            name='height',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Высота'),
        ),
        migrations.AddField(
            model_name='product',
            name='led_generation',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Поколение светодиодов'),
        ),
        migrations.AddField(
            model_name='product',
            name='length',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Длина, мм'),
        ),
        migrations.AddField(
            model_name='product',
            name='luminous_flux',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Световой поток'),
        ),
        migrations.AddField(
            model_name='product',
            name='operating_voltage',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Рабочее напряжение '),
        ),
        migrations.AddField(
            model_name='product',
            name='plinth_type',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Тип цоколя'),
        ),
        migrations.AddField(
            model_name='product',
            name='power_consumption',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Потребляемость ВТ'),
        ),
        migrations.AddField(
            model_name='product',
            name='profile_tube_size',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Размер профильной трубы, мм'),
        ),
        migrations.AddField(
            model_name='product',
            name='protection_level',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Степень защиты'),
        ),
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Размер'),
        ),
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='category_images/', verbose_name='Фото Категории'),
        ),
        migrations.AlterField(
            model_name='product',
            name='body_material',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Материал корпуса'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='core.category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='coating',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Покрытие'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='product_images/', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='product',
            name='wind_region',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Ветровой район'),
        ),
        migrations.AlterField(
            model_name='projectphoto',
            name='image',
            field=models.ImageField(upload_to='project_images/'),
        ),
    ]

# Generated by Django 4.2.3 on 2023-08-31 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_advetisements', '0006_advertisements_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='advertisements',
            old_name='tittle',
            new_name='title',
        ),
        migrations.AlterField(
            model_name='advertisements',
            name='image',
            field=models.ImageField(upload_to='advertisements/', verbose_name='Изображение'),
        ),
    ]
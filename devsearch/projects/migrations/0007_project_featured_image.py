# Generated by Django 4.0.1 on 2022-01-14 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_remove_project_featured_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='featured_image',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to=''),
        ),
    ]

# Generated by Django 4.2.4 on 2023-08-28 13:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('appname', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enrolledclasses',
            name='student',
        ),
        migrations.AddField(
            model_name='enrolledclasses',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

# Generated by Django 2.0.7 on 2018-07-04 06:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('motion_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postitem',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
    ]

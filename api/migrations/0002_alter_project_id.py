# Generated by Django 4.2.2 on 2023-09-21 12:26

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='id',
            field=models.UUIDField(default=uuid.UUID('b49731e1-bf3d-4618-9537-7a131f8d8d98'), editable=False, primary_key=True, serialize=False),
        ),
    ]

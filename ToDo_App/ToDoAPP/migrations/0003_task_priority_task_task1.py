# Generated by Django 4.1.3 on 2022-12-04 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ToDoAPP', '0002_task_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='priority',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='task1',
            field=models.TextField(default='A'),
            preserve_default=False,
        ),
    ]

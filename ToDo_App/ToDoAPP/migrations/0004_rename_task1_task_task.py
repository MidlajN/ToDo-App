# Generated by Django 4.1.3 on 2022-12-04 18:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ToDoAPP', '0003_task_priority_task_task1'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='task1',
            new_name='task',
        ),
    ]

# Generated by Django 4.2.6 on 2023-10-22 14:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("todo_app", "0011_alter_todoitem_due_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="todoitem",
            name="due_date",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 10, 29, 14, 4, 23, 708223)
            ),
        ),
    ]

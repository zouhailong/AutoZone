# Generated by Django 2.1.5 on 2019-08-08 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0003_auto_20190805_1040'),
    ]

    operations = [
        migrations.AddField(
            model_name='singel_apis_task',
            name='task_status_code',
            field=models.CharField(max_length=200, null=True, verbose_name='状态码'),
        ),
    ]

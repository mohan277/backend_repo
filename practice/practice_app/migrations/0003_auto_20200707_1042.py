# Generated by Django 3.0.5 on 2020-07-07 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('practice_app', '0002_persondetails_color_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persondetails',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]

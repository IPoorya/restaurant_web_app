# Generated by Django 4.2.3 on 2023-07-27 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_otpcode_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otpcode',
            name='created_at',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='date_joined',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]

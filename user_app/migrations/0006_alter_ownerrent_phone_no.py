# Generated by Django 4.1.7 on 2023-03-03 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0005_ownerrent_phone_no_ownerrent_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ownerrent',
            name='phone_no',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]

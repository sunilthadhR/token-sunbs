# Generated by Django 4.2.16 on 2024-10-29 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spack', '0008_remove_token_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='token',
            name='token',
            field=models.CharField(max_length=20, null=True, unique=True),
        ),
    ]

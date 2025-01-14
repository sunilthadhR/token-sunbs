# Generated by Django 4.2.16 on 2024-10-29 09:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('spack', '0006_alter_user_pack'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='price',
            field=models.IntegerField(blank=True, choices=[('499', 'basic'), ('599', 'premium'), ('699', 'vip'), ('799', 'vvip'), ('899', 'live pack')], null=True),
        ),
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=20, unique=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='token', to='spack.user')),
            ],
        ),
    ]

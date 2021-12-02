# Generated by Django 2.2.24 on 2021-11-29 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_cart_and_cartproduct_model'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='last_name',
        ),
        migrations.AddField(
            model_name='profile',
            name='nickname',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='points',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=30),
        ),
        migrations.AddField(
            model_name='profile',
            name='rating',
            field=models.DecimalField(decimal_places=1, default=4.0, max_digits=2),
        ),
    ]

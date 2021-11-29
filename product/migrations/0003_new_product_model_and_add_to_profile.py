# Generated by Django 2.2.24 on 2021-11-24 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=100, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('description', models.TextField(max_length=500)),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='first_name',
            field=models.TextField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='last_name',
            field=models.TextField(max_length=30, null=True),
        ),
    ]

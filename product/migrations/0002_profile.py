# Generated by Django 2.2.24 on 2021-11-02 14:42

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


def assign_users(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    Profile = apps.get_model('product', 'Profile')
    for user in User.objects.all():
        profile, created = Profile.objects.get_or_create(user=user)
        profile.save()


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0001_model_navbar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('bio', models.TextField(blank=True, max_length=500)),
                ('location', models.CharField(blank=True, max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RunPython(assign_users, migrations.RunPython.noop),
    ]

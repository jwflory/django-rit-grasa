# Generated by Django 2.2.6 on 2019-10-18 02:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='userInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('org_name', models.CharField(max_length=255)),
                ('isAdmin', models.BooleanField(default=False)),
                ('isActive', models.BooleanField(default=False)),
                ('isPending', models.BooleanField(default=True)),
                ('image_reference', models.CharField(default='', max_length=40)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='NOT SPECIFIED', max_length=255)),
                ('content', models.TextField(default='NOT SPECIFIED')),
                ('address', models.CharField(default='NOT SPECIFIED', max_length=255)),
                ('lat', models.CharField(default='43.154535', max_length=255)),
                ('lng', models.CharField(default='-77.590575', max_length=255)),
                ('website', models.CharField(default='NOT SPECIFIED', max_length=255)),
                ('fees', models.CharField(default='NOT SPECIFIED', max_length=255)),
                ('isPending', models.BooleanField(default=True)),
                ('contact_name', models.CharField(default='NOT SPECIFIED', max_length=255)),
                ('contact_email', models.CharField(default='NOT SPECIFIED', max_length=255)),
                ('contact_phone', models.CharField(default='NOT SPECIFIED', max_length=255)),
                ('editOf', models.IntegerField(default=0)),
                ('categories', models.ManyToManyField(to='grasa_event_locator.Category')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grasa_event_locator.userInfo')),
            ],
        ),
    ]
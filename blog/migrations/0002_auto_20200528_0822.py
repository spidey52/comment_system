# Generated by Django 3.0.6 on 2020-05-28 02:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='authors',
            new_name='author',
        ),
    ]
# Generated by Django 4.1.4 on 2022-12-08 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='nickname',
            field=models.CharField(default='<django.db.models.fields.related.OneToOneField>', max_length=50),
        ),
    ]

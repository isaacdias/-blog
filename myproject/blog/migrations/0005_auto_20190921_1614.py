# Generated by Django 2.2.5 on 2019-09-21 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_upload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='upload',
            field=models.ImageField(upload_to='images/'),
        ),
    ]

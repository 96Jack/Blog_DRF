# Generated by Django 3.2.13 on 2022-08-31 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cbv_blog', '0003_alter_post_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=128),
        ),
    ]
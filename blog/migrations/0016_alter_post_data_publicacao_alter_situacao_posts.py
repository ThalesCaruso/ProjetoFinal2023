# Generated by Django 4.1.7 on 2023-05-26 23:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_alter_post_data_publicacao_postsituacao_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='data_publicacao',
            field=models.DateTimeField(verbose_name=datetime.datetime(2023, 5, 26, 23, 28, 57, 274126, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='situacao',
            name='posts',
            field=models.ManyToManyField(through='blog.PostSituacao', to='blog.post'),
        ),
    ]
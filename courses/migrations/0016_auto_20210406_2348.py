# Generated by Django 3.1.1 on 2021-04-06 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_auto_20210405_1908'),
        ('courses', '0015_auto_20210406_2212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='dislikes',
            field=models.ManyToManyField(blank=True, related_name='dislikes_post', to='student.studentProfile'),
        ),
        migrations.AlterField(
            model_name='video',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='likes_post', to='student.studentProfile'),
        ),
    ]

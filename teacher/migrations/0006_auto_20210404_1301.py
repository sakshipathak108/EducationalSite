# Generated by Django 3.1.1 on 2021-04-04 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0005_auto_20210404_1301'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teacherprofile',
            old_name='name',
            new_name='lastname',
        ),
        migrations.AddField(
            model_name='teacherprofile',
            name='firstname',
            field=models.CharField(default='pp', max_length=100),
        ),
    ]
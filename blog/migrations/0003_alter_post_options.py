# Generated by Django 3.2.10 on 2022-01-03 17:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20220103_1017'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-published_date']},
        ),
    ]

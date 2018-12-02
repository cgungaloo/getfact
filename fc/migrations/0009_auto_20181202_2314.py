# Generated by Django 2.1.2 on 2018-12-02 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fc', '0008_auto_20181202_2309'),
    ]

    operations = [
        migrations.AddField(
            model_name='reportcomment',
            name='investigated',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='reportcomment',
            name='resolution',
            field=models.TextField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='reportfact',
            name='investigated',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='reportfact',
            name='resolution',
            field=models.TextField(max_length=300, null=True),
        ),
    ]

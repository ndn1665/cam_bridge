# Generated by Django 4.2.3 on 2024-05-17 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0009_womeninfo_keyword_alter_meninfo_w_face_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='matchinghistory',
            name='r_no',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

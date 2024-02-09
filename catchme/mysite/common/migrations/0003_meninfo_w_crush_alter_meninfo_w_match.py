# Generated by Django 4.2.3 on 2024-02-09 12:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_rename_gender_userinfo_ismale'),
    ]

    operations = [
        migrations.AddField(
            model_name='meninfo',
            name='w_crush',
            field=models.ForeignKey(blank=True, db_column='w_crush', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='m_crush', to='common.womeninfo'),
        ),
        migrations.AlterField(
            model_name='meninfo',
            name='w_match',
            field=models.ForeignKey(blank=True, db_column='w_match', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='m_matched', to='common.womeninfo'),
        ),
    ]

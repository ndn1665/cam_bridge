# Generated by Django 4.2.3 on 2024-02-09 13:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='menInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nickname', models.CharField(max_length=50)),
                ('chat', models.CharField(blank=True, max_length=10, null=True)),
                ('age', models.IntegerField(null=True)),
                ('job', models.CharField(blank=True, max_length=50, null=True)),
                ('school', models.CharField(blank=True, max_length=50, null=True)),
                ('major', models.CharField(blank=True, max_length=50, null=True)),
                ('mbti', models.CharField(blank=True, max_length=10, null=True)),
                ('army', models.CharField(blank=True, max_length=10, null=True)),
                ('height', models.IntegerField(blank=True, null=True)),
                ('body', models.CharField(blank=True, max_length=10, null=True)),
                ('eyes', models.CharField(blank=True, max_length=10, null=True)),
                ('face', models.CharField(blank=True, max_length=10, null=True)),
                ('hobby', models.CharField(blank=True, max_length=100, null=True)),
                ('animal', models.CharField(blank=True, max_length=20, null=True)),
                ('ready', models.BooleanField(default=False)),
                ('avgage', models.IntegerField(null=True)),
                ('w_age', models.CharField(blank=True, max_length=50, null=True)),
                ('w_job', models.CharField(blank=True, max_length=50, null=True)),
                ('w_school', models.CharField(blank=True, max_length=50, null=True)),
                ('w_major', models.CharField(blank=True, max_length=50, null=True)),
                ('w_mbti', models.CharField(blank=True, max_length=10, null=True)),
                ('w_height', models.IntegerField(blank=True, null=True)),
                ('w_body', models.CharField(blank=True, max_length=10, null=True)),
                ('w_eyes', models.CharField(blank=True, max_length=10, null=True)),
                ('w_face', models.CharField(blank=True, max_length=10, null=True)),
                ('w_hobby', models.CharField(blank=True, max_length=100, null=True)),
                ('w_animal', models.CharField(blank=True, max_length=20, null=True)),
                ('free', models.TextField(blank=True, null=True)),
                ('kakaotalk_id', models.CharField(blank=True, max_length=20, null=True)),
                ('link', models.CharField(blank=True, max_length=20, null=True)),
                ('coin', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='room',
            fields=[
                ('rno', models.AutoField(primary_key=True, serialize=False)),
                ('rname', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('meetingnum', models.IntegerField(default=0)),
                ('readynum', models.IntegerField(default=0)),
                ('location', models.CharField(blank=True, max_length=50, null=True)),
                ('matching', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='userInfo',
            fields=[
                ('kid', models.BigIntegerField(db_index=True, primary_key=True, serialize=False)),
                ('location', models.CharField(max_length=50)),
                ('ismale', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='womenInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nickname', models.CharField(max_length=50)),
                ('chat', models.CharField(blank=True, max_length=10, null=True)),
                ('age', models.IntegerField(null=True)),
                ('job', models.CharField(blank=True, max_length=50, null=True)),
                ('school', models.CharField(blank=True, max_length=50, null=True)),
                ('major', models.CharField(blank=True, max_length=50, null=True)),
                ('mbti', models.CharField(blank=True, max_length=10, null=True)),
                ('height', models.IntegerField(blank=True, null=True)),
                ('body', models.CharField(blank=True, max_length=10, null=True)),
                ('eyes', models.CharField(blank=True, max_length=10, null=True)),
                ('face', models.CharField(blank=True, max_length=10, null=True)),
                ('hobby', models.CharField(blank=True, max_length=100, null=True)),
                ('animal', models.CharField(blank=True, max_length=20, null=True)),
                ('ready', models.BooleanField(default=False)),
                ('avgage', models.IntegerField(null=True)),
                ('m_age', models.CharField(blank=True, max_length=50, null=True)),
                ('m_job', models.CharField(blank=True, max_length=50, null=True)),
                ('m_school', models.CharField(blank=True, max_length=50, null=True)),
                ('m_major', models.CharField(blank=True, max_length=50, null=True)),
                ('m_mbti', models.CharField(blank=True, max_length=10, null=True)),
                ('m_army', models.CharField(blank=True, max_length=10, null=True)),
                ('m_height', models.IntegerField(blank=True, null=True)),
                ('m_body', models.CharField(blank=True, max_length=10, null=True)),
                ('m_eyes', models.CharField(blank=True, max_length=10, null=True)),
                ('m_face', models.CharField(blank=True, max_length=10, null=True)),
                ('m_hobby', models.CharField(blank=True, max_length=100, null=True)),
                ('m_animal', models.CharField(blank=True, max_length=20, null=True)),
                ('free', models.TextField(blank=True, null=True)),
                ('kakaotalk_id', models.CharField(blank=True, max_length=20, null=True)),
                ('link', models.CharField(blank=True, max_length=20, null=True)),
                ('coin', models.IntegerField(default=0)),
                ('m_match', models.ForeignKey(blank=True, db_column='m_match', null=True, on_delete=django.db.models.deletion.SET_NULL, to='common.meninfo')),
                ('participate_room', models.ForeignKey(blank=True, db_column='participate_room', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='women_infos', to='common.room')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.userinfo')),
            ],
        ),
        migrations.CreateModel(
            name='womenParty',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('age', models.IntegerField(null=True)),
                ('animal', models.CharField(blank=True, max_length=20, null=True)),
                ('job', models.CharField(blank=True, max_length=50, null=True)),
                ('school', models.CharField(blank=True, max_length=50, null=True)),
                ('major', models.CharField(blank=True, max_length=50, null=True)),
                ('height', models.IntegerField(blank=True, null=True)),
                ('body', models.CharField(blank=True, max_length=10, null=True)),
                ('leader_woman', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='women_party', to='common.womeninfo')),
            ],
        ),
        migrations.CreateModel(
            name='payment',
            fields=[
                ('tid', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('pay_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='payment', to='common.userinfo')),
            ],
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('notice', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.userinfo')),
            ],
        ),
        migrations.CreateModel(
            name='menParty',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('age', models.IntegerField(null=True)),
                ('animal', models.CharField(blank=True, max_length=20, null=True)),
                ('job', models.CharField(blank=True, max_length=50, null=True)),
                ('school', models.CharField(blank=True, max_length=50, null=True)),
                ('major', models.CharField(blank=True, max_length=50, null=True)),
                ('height', models.IntegerField(blank=True, null=True)),
                ('body', models.CharField(blank=True, max_length=10, null=True)),
                ('selected', models.BooleanField(default=False)),
                ('leader_man', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='men_party', to='common.meninfo')),
            ],
        ),
        migrations.AddField(
            model_name='meninfo',
            name='participate_room',
            field=models.ForeignKey(blank=True, db_column='participate_room', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='men_infos', to='common.room'),
        ),
        migrations.AddField(
            model_name='meninfo',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.userinfo'),
        ),
        migrations.AddField(
            model_name='meninfo',
            name='w_crush',
            field=models.ForeignKey(blank=True, db_column='w_crush', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='m_crush', to='common.womeninfo'),
        ),
        migrations.AddField(
            model_name='meninfo',
            name='w_match',
            field=models.ForeignKey(blank=True, db_column='w_match', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='m_matched', to='common.womeninfo'),
        ),
        migrations.CreateModel(
            name='matchingInfo',
            fields=[
                ('matchingnum', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('matched_man', models.ForeignKey(blank=True, db_column='matched_man', null=True, on_delete=django.db.models.deletion.SET_NULL, to='common.meninfo')),
                ('matched_room', models.ForeignKey(blank=True, db_column='matched_room', null=True, on_delete=django.db.models.deletion.SET_NULL, to='common.room')),
                ('matched_woman', models.ForeignKey(blank=True, db_column='matched_woman', null=True, on_delete=django.db.models.deletion.SET_NULL, to='common.womeninfo')),
            ],
        ),
    ]

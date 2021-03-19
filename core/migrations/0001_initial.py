# Generated by Django 2.1.3 on 2019-03-29 14:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('director', models.CharField(max_length=100, verbose_name='导演')),
                ('score', models.CharField(max_length=100, verbose_name='评分')),
                ('name', models.CharField(max_length=100, verbose_name='名称')),
                ('movietype', models.CharField(max_length=100, verbose_name='类型')),
                ('img', models.CharField(default='', max_length=500, verbose_name='图片')),
            ],
            options={
                'verbose_name': '电影表',
                'verbose_name_plural': '电影表',
            },
        ),
        migrations.CreateModel(
            name='MovieUserComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=1000, verbose_name='评论')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Movie', verbose_name='电影')),
            ],
        ),
        migrations.CreateModel(
            name='MovieUserScore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.CharField(default='', max_length=100, verbose_name='分数')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Movie', verbose_name='电影')),
            ],
            options={
                'verbose_name': '用户评分表',
                'verbose_name_plural': '用户评分表',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='姓名')),
                ('username', models.CharField(max_length=100, verbose_name='用户名')),
                ('password', models.CharField(max_length=100, verbose_name='密码')),
                ('mobile', models.CharField(max_length=100, verbose_name='手机号')),
                ('interesting', models.CharField(max_length=500, verbose_name='兴趣爱好')),
            ],
            options={
                'verbose_name': '用户表',
                'verbose_name_plural': '用户表',
            },
        ),
        migrations.AddField(
            model_name='movieuserscore',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.User', verbose_name='用户'),
        ),
        migrations.AddField(
            model_name='movieusercomment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.User', verbose_name='用户'),
        ),
    ]
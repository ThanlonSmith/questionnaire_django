# Generated by Django 3.0.8 on 2020-08-07 08:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClassList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='班级名称')),
            ],
        ),
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('times', models.PositiveSmallIntegerField(verbose_name='第几次问卷调查')),
                ('count', models.PositiveSmallIntegerField(verbose_name='生成多少个唯一码')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='添加的时间')),
                ('grade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.ClassList', verbose_name='外键关联班级表')),
            ],
        ),
        migrations.CreateModel(
            name='SurveyCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_code', models.CharField(max_length=10, unique=True, verbose_name='唯一码')),
                ('is_used', models.BooleanField(default=False, verbose_name='是否已经被使用')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='添加的时间')),
                ('survey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Survey', verbose_name='外键关联问卷调查表')),
            ],
        ),
        migrations.CreateModel(
            name='SurveyQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('survey_type', models.CharField(choices=[('choice', '单选'), ('suggest', '建议')], max_length=32, verbose_name='问题的类型')),
                ('name', models.CharField(max_length=64, verbose_name='问题的名称')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='添加的时间')),
            ],
        ),
        migrations.CreateModel(
            name='SurveyTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='班级名称')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='添加的时间')),
                ('question', models.ManyToManyField(to='app.SurveyQuestion', verbose_name='多对多关联调查问卷问题表')),
            ],
        ),
        migrations.CreateModel(
            name='SurveyRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='得分')),
                ('content', models.CharField(blank=True, max_length=1024, null=True, verbose_name='内容')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='添加的时间')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.SurveyQuestion', verbose_name='外键关联问卷的问题表')),
                ('survey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Survey', verbose_name='外键关联问卷调查表')),
                ('survey_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.SurveyCode', verbose_name='外键关联唯一码表')),
            ],
        ),
        migrations.CreateModel(
            name='SurveyChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='选项的名称')),
                ('score', models.PositiveSmallIntegerField(verbose_name='分值')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='添加的时间')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.SurveyQuestion', verbose_name='外键关联调查问卷问题表')),
            ],
        ),
        migrations.AddField(
            model_name='survey',
            name='survey_template',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.SurveyTemplate', verbose_name='外键关联的模板表'),
        ),
    ]

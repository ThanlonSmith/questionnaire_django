# Generated by Django 3.0.8 on 2020-08-07 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='survey',
            name='survey_template',
        ),
        migrations.AddField(
            model_name='survey',
            name='survey_template',
            field=models.ManyToManyField(blank=True, to='app.SurveyTemplate', verbose_name='外键关联的模板表'),
        ),
    ]
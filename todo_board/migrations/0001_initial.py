# Generated by Django 3.0.3 on 2020-03-09 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TbProjectCode',
            fields=[
                ('pcode', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('pname', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'tb_project_code',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TbTodoList',
            fields=[
                ('no', models.AutoField(primary_key=True, serialize=False)),
                ('pcode', models.CharField(blank=True, max_length=4, null=True)),
                ('user_id', models.CharField(blank=True, max_length=50, null=True)),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('is_complete', models.IntegerField(blank=True, null=True)),
                ('priority', models.IntegerField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'tb_todo_list',
                'managed': False,
            },
        ),
    ]

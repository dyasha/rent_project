# Generated by Django 2.2.19 on 2022-08-23 14:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='price',
            field=models.IntegerField(default=1000, verbose_name='Цена'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='post',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='posts', to='posts.Group', verbose_name='Группа'),
        ),
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации'),
        ),
        migrations.AlterField(
            model_name='post',
            name='room_type',
            field=models.CharField(choices=[('P', 'Панельный'), ('K', 'Кирпичный'), ('MK', 'Монолитно-Кирпичный'), ('M', 'Монолитный')], max_length=42, verbose_name='Тип Помещения'),
        ),
        migrations.AlterField(
            model_name='post',
            name='square',
            field=models.FloatField(verbose_name='Площадь'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Заголовок'),
        ),
    ]

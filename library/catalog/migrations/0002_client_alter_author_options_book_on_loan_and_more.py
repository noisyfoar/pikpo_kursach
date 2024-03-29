# Generated by Django 4.2.1 on 2023-05-31 08:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='Имя автора')),
                ('last_name', models.CharField(max_length=100, verbose_name='Фамилия автора')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
                'ordering': ['last_name', 'first_name'],
            },
        ),
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['last_name', 'first_name'], 'verbose_name': 'Автор', 'verbose_name_plural': 'Авторы'},
        ),
        migrations.AddField(
            model_name='book',
            name='on_loan',
            field=models.BooleanField(default=False, null=True, verbose_name='Во временное пользование'),
        ),
        migrations.AddField(
            model_name='book',
            name='return_date',
            field=models.DateField(blank=True, null=True, verbose_name='Дата возвращения книги'),
        ),
        migrations.AlterField(
            model_name='book',
            name='summary',
            field=models.TextField(blank=True, default='', max_length=1000, verbose_name='Краткое описание'),
        ),
        migrations.AddField(
            model_name='book',
            name='client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.client', verbose_name='Клиент'),
        ),
    ]

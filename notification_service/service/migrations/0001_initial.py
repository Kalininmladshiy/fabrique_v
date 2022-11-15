# Generated by Django 4.1.3 on 2022-11-15 12:04

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(max_length=200, verbose_name='ФИО владельца')),
                ('phonenumber', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None, verbose_name='номер телефона')),
                ('mobile_operator_code', models.IntegerField(blank=True, null=True, verbose_name='код мобильного оператора')),
                ('timezone', models.CharField(blank=True, default='0', max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Mailing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('launched_at', models.DateTimeField(blank=True, null=True, verbose_name='время запуска')),
                ('text', models.TextField(blank=True, verbose_name='текст сообщения')),
                ('completed_at', models.DateTimeField(blank=True, null=True, verbose_name='время завершения')),
                ('clients', models.ManyToManyField(blank=True, related_name='mailings', to='service.client', verbose_name='кому отправили')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, unique=True, verbose_name='Тег')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('send_status', models.BooleanField(null=True, verbose_name='Отправлено ли сообщение')),
                ('clients', models.ManyToManyField(blank=True, related_name='messages', to='service.client', verbose_name='кому отправили')),
                ('mailing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='message', to='service.mailing', verbose_name='В какой рассылке')),
            ],
        ),
        migrations.AddField(
            model_name='client',
            name='tags',
            field=models.ManyToManyField(related_name='clients', to='service.tag', verbose_name='Теги'),
        ),
    ]

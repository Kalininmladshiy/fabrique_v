from django.db import models
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField


class Mailing(models.Model):
    launched_at = models.DateTimeField(
        verbose_name='время запуска',
        null=True,
        blank=True,
     )
    text = models.TextField(
        verbose_name='текст сообщения',
        blank=True,
     )
    clients = models.ManyToManyField(
        'Client',
        verbose_name='кому отправили',
        related_name='mailings',
        blank=True,
    )
    completed_at = models.DateTimeField(
        verbose_name='время завершения',
        null=True,
        blank=True,
     )

    def __str__(self):
        return self.text


class Client(models.Model):
    fio = models.CharField('ФИО владельца', max_length=200)
    phonenumber = PhoneNumberField('номер телефона', blank=True)
    mobile_operator_code = models.IntegerField(verbose_name='код мобильного оператора', null=True, blank=True)
    tags = models.ManyToManyField(
        'Tag',
        related_name='clients',
        verbose_name='Теги')
    timezone = models.CharField(max_length=3, default="0", blank=True)

    def __str__(self):
        return self.fio    


class Message(models.Model):
    mailing = models.ForeignKey(
        'Mailing',
        verbose_name='В какой рассылке',
        related_name='message',
        on_delete=models.CASCADE,
     )
    send_status = models.BooleanField('Отправлено ли сообщение', null=True)
    clients = models.ManyToManyField(
        'Client',
        verbose_name='кому отправили',
        related_name='messages',
        blank=True,
    )

    def __str__(self):
        return self.mailing.text


class Tag(models.Model):
    title = models.CharField('Тег', max_length=20, unique=True)

    def __str__(self):
        return self.title

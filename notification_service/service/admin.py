from django.contrib import admin

from .models import Mailing, Client, Message, Tag


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    search_fields = ('id', 'text')
    list_display = ('launched_at','text')
    list_filter = ('launched_at', 'completed_at')
    raw_id_fields = ('clients',)

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    search_fields = ('fio', 'phonenumber')
    list_display = ('fio','phonenumber')
    list_filter = ('timezone', 'mobile_operator_code')    
    raw_id_fields = ('tags',)

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id','send_status')
    list_filter = ('send_status',)    
    raw_id_fields = ('clients',)    

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ('title',)

from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse("Привет! Перейди в админку для добавления клиентов и рассылок.")

from django.shortcuts import render
from django.http import HttpResponse


def projects(request):
    return HttpResponse('Aqui está nossos produtos')


def project(request, pk):
    return HttpResponse('Single Project' + ' ' + f'{pk}')

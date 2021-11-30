from django.contrib import admin
from django.urls import path
from django.http import HttpResponse


def projects(request):
    return HttpResponse('Aqui está nossos produtos')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', projects, name="projects"),

]

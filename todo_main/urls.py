from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from todo_main import views

app_name = "todo_main"

urlpatterns = [
    url(r'^$', views.Todo_main.as_view(), name='todo_main')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
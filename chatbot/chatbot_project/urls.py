from django.contrib import admin
from django.urls import path

from chatbot_app.views import chat_view

urlpatterns = [
    path("", chat_view, name="chat-home"),
    path("admin/", admin.site.urls),
]

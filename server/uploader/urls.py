from django.urls import path

from . import views

urlpatterns = [
    path('', views.UploadImageView.as_view()),
]
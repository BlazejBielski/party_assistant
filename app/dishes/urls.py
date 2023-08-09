from django.urls import path

from . import views

app_name = "dishes"

urlpatterns = [
    path("soups", views.SoupsView.as_view(), name='soups')
]

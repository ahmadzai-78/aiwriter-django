from django.urls import path
from .views import writer_view

urlpatterns = [
    path('', writer_view, name='writer'),
]

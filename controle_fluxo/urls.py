from django.urls import path
from .views import IndexView, CreateActivy

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('create_activity', CreateActivy.as_view(), name='create_activity')
]
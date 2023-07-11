from django.urls import path
from .views import IndexView, CreateActivity, HistoricView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('create_activity', CreateActivity.as_view(), name='create_activity'),
    path('historic/<str:name>', HistoricView.as_view(), name='historic'),
]
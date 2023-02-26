from django.urls import path

from . import views

app_name = 'dashboard'
urlpatterns=[
    path('', views.IndexView.as_view(),name='index'),
    path('asset_summary', views.SummaryView.as_view(), name='summary'),
]
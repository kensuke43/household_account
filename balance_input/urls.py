from django.urls import path

from . import views

app_name = 'balance_input'
urlpatterns=[
    path('', views.Balance_input_View.as_view(),name='input')
]
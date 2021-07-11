from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name ='index'),
    path('submit_query',views.submit_query,name='submit_query'),
]
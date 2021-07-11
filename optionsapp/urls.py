from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name ='index'),
    path('submitquery',views.submitquery,name='submitquery'),
    path('sortdata',views.sortdata,name='sortdata'),
]
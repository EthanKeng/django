from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('about/',views.about,name='about'),
    path('addAdress',views.addAdress,name='addAdress'),
    path('reqYhaoo/',views.reqYahoo,name='req'),
]

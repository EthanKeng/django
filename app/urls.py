from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('about/',views.about,name='about'),
    path('addCard/',views.addCard,name='addCard'),
    path('card/',views.card,name='card'),
    path('reqYhaoo/',views.reqYahoo,name='req'),
    path('edit/<list_id>',views.edit,name="edit"),
    path('delete/<list_id>',views.delete,name='delete')
]

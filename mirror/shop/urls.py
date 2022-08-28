from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('cloth_img', views.cloth_img, name='cloth_img'),
    path('cloth_data',views.cloth_data,name='cloth_data'),
    path('user_selectCloth',views.user_selectCloth,name='user_selectCloth'),
    path('user_show',views.user_show,name='user_show'),
]
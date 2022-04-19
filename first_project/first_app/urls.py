from django.urls import path
from first_app import views

app_name='first_app'

urlpatterns = [
    path('',views.index,name='index'),
    path('picture/',views.picture,name='picture'),
    path('other/',views.other,name='other'),
    path('base/',views.base,name='base'),
    path('relative/',views.relative,name='relative'),
    path('register/',views.register,name='register'),
    path('user_login/',views.user_login,name='user_login'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('city/', views.city, name="city"),
    path('comments/', views.comments, name="comment"),
    path('list/', views.list, name="list"),
    path('mcomm/', views.makecomm, name="mc"),
    path('place/', views.place, name="place"),
    path('signin/', views.signin, name="si"),
    path('signup', views.signup, name="su"),
    path('howtogo/',views.howToGo, name="howTo")

]

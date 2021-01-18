from django.urls import path
from . import views
from .views import Istanbul, PPlace,Ankara,Izmir

urlpatterns = [
    path('', views.home, name="home"),
    path('city/', views.city, name="city"),
    path('Istanbul/', Istanbul.as_view(),name='Istanbul'),
    path('comments/', views.comments, name="comment"),
    path('list/', views.list, name="list"),
    path('makecomm/', views.makecomm, name="mc"),
    path('place/', views.place, name="place"),
    path('signin/', views.signin, name="si"),
    path('signup', views.signup, name="su"),
    path('howtogo/', views.howToGo, name="howTo"),
    path('logout/', views.logoutUser,name="logout"),
    path('whtg/', views.whtg, name = 'whtg'),
    path('cPlace/', views.createPlace, name = 'createPlace'),
    path('PPlace/<int:pk>', PPlace.as_view(),name='PPlaces'),
    path('Izmir/', Izmir.as_view(),name='Izmir'),
    path('Ankara/', Ankara.as_view(),name='Ankara'),
]

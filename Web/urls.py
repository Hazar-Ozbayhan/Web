from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('city/', views.city, name="city"),
    path('comments/', views.comments, name="comment"),
    path('list/', views.list, name="list"),
    path('makecomm/', views.makecomm, name="mc"),
    path('place/', views.place, name="place"),
    path('signin/', views.signin, name="si"),
    path('signup', views.signup, name="su"),
    path('howtogo/', views.howToGo, name="howTo"),
    path('logout/', views.logoutUser,name="logout"),
    path('l', views.homel, name="homel"),
    path('cityl/', views.cityl, name="cityl"),
    path('commentsl/', views.commentsl, name="commentl"),
    path('placel/', views.placel, name="placel"),
    path('howtogol/', views.howToGol, name="howTol"),
    path('whtg/', views.whtg, name = 'whtg'),
    path('cPlace/', views.createPlace, name = 'createPlace'),
]

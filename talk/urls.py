from django.urls import path , include
from . import views


app_name = 'talk'

urlpatterns = [
    path('',views.home , name='home'),
    path('d/',views.d , name='d'),
    path('<slug:post>/', views.post_single, name='post_single'),
    path('category/<category>/', views.CatListView.as_view(), name='category'),
    path('ques',views.question , name='question'),
    path('album', views.album, name = 'album-list'),
    path('album/like',views.like , name='like-album'),
    path('contact',views.contact , name='contact'),
    path('fav/<int:id>/',views.favourite_add , name='favourite_add'),
    path('profile/favourites',views.favourite_list ,name='favourite_list'),

]
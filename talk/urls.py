from django.urls import path , include
from . import views


app_name = 'talk'

urlpatterns = [
    # path('',views.home , name='home'),
    path('d/',views.d , name='d'),
    path('', views.home, name='homepage'),
    path('<slug:post>/', views.post_single, name='post_single'),
    path('category/<category>/', views.CatListView.as_view(), name='category'),
    path('ques',views.question , name='question'),
]
from django.contrib import admin
from django.urls import path
from . import views

app_name='youtube'

urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    path('detail/<int:pk>',views.detailfunc,name='detail'),
    path('create/',views.CreateView.as_view(),name='create'),
    path('delete/<int:pk>',views.DeleteView.as_view(),name='delete'),
    path('update/<int:pk>',views.UpdateView.as_view(),name='update'),
    path('signup/',views.signupfunc,name='signup'),
    path('login/',views.loginfunc,name='login'),
    path('logout/',views.logoutfunc,name='logout'),
    path('good/<int:pk>',views.goodfunc,name='good'),
    path('mypage/<int:pk>',views.MypageView.as_view(),name='mypage'),
    path('comment/<int:post_pk>',views.CommentView.as_view(),name='comment'),
    
]
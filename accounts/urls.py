from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name="signup"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('<str:user_name>/', views.mypage, name="mypage"),
    path('<str:user_name>/edit/', views.edit, name="edit"),
    path('<str:user_name>/password/', views.password, name="password"),
]
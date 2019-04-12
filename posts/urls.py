from django.urls import path
from . import views
app_name = 'posts'


urlpatterns = [
    path('', views.list, name="list"),
    path('create/', views.create, name="create"),
    path('<int:post_pk>/', views.detail, name="detail"),
    path('edit/<int:post_pk>/', views.edit, name="edit"),
    path('delete/<int:post_pk>/', views.delete, name="delete"),
]

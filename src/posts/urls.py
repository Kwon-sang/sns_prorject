from django.urls import path

from . import views
from .views import PostListView

app_name = 'posts'

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('create/', views.post_create, name='post_create'),
    path('delete/<int:id>/', views.post_delete, name='post_delete'),
    path('update/<int:id>/', views.post_update, name='post_update'),
]
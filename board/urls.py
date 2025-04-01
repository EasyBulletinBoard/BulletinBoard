from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.board_list, name='board_list'),
    path('<int:board_id>/', views.board_detail, name='board_detail'),
    path('create/', views.create_board, name='create_board'),
    path('<int:board_id>/create_card/', views.create_card, name='create_card'),
    path('<int:board_id>/add_member/', views.add_member, name='add_member'),
    path("settings/", views.settings, name="settings"),
    path("boards/<int:board_id>/like/", views.like_board, name="like_board"),
]
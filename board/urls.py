from django.urls import path
from . import views

urlpatterns = [
    path("", views.board_list, name="board_list"),
    path("create/", views.create_board, name="create_board"),
    path("<int:board_id>/", views.board_detail, name="board_detail"),
    path("<int:board_id>/create_card/", views.create_card, name="create_card"),
    path("<int:board_id>/add_member/", views.add_member, name="add_member"),
    path("signup/", views.signup, name="signup"),
    path("settings/", views.settings, name="settings"),
    path("cards/<int:card_id>/like/", views.like_card, name="like_card"),
    path("cards/<int:card_id>/delete/", views.delete_card, name="delete_card"),
]
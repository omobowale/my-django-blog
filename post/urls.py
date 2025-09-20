from django.urls import path
from .views import posts_list, new_post, single_post, edit_post, delete_post

urlpatterns = [
    path("posts/", posts_list, name="posts_list"),
    path("posts/new", new_post, name="new_post"),
    path("posts/<int:post_id>", single_post, name="single_post"),
    path("posts/<int:post_id>/edit", edit_post, name="edit_post"),
    path("posts/<int:post_id>/delete", delete_post, name="delete_post") 
]
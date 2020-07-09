from django.urls import path

from .views import (
    create_post_function,
    get_post_function,
    create_reply_to_comment,
    create_reaction_to_post,
    create_reaction_to_comment,
    delete_post_function,
    create_comment_function,
    set_timezone
    )
from . import views

urlpatterns = [
    path('post/', create_post_function),
    path('post/<int:post_id>/', get_post_function),
    path('comment/<int:comment_id>/reply/create/', create_reply_to_comment),
    path('post/<int:post_id>/react/', create_reaction_to_post),
    path('comment/<int:comment_id>/react/', create_reaction_to_comment),
    path('post/<int:post_id>/delete/', delete_post_function),
    path('post/<int:post_id>/comment/create/', create_comment_function),
    path('timezone/',views.set_timezone,name='set_timezone'),
    ]
from django.urls import path
from posts.views import *

urlpatterns = [
    # path('', hello_world, name = 'hello_world'),
    path('introduction/', introduction, name = 'introduction'),

    path('', get_post_all, name = 'post_all'),
    # path('<int:id>/', get_post_detail, name = 'post_detail'),
    path('<int:id>/', post_detail, name = 'post_detail'),
    path('new/', create_post, name = 'create_post'),
    path('comment/<int:id>/', get_comment, name = 'get_comment'),
    path('new_comment/<int:post_id>/', create_comment, name = 'create_comment'),
    path('recent/', get_recent_post, name = 'get_recent_post')
]
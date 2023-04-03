from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

router_v1 = DefaultRouter()

router_v1.register(r'posts', PostViewSet, basename='PostViewSet')
router_v1.register(r'posts/(?P<post_id>\d+)/comments',
                   CommentViewSet, basename='CommentViewSet')
router_v1.register(r'posts/(?P<post_id>\d+)/comments/(?P<comment_id>\d+)',
                   CommentViewSet, basename='CommentViewSet')
router_v1.register(r'groups', GroupViewSet, basename='GroupViewSet')
router_v1.register(r'groups/(?P<group_id>\d+)',
                   GroupViewSet, basename='GroupViewSet')
router_v1.register(r'follow', FollowViewSet, basename='FollowViewSet')


urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/auth/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]

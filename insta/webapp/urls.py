from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from webapp.views.post import CreatePostView, UserProfileView, UserSubscribeView
from webapp.views.base import ProfileView
from webapp.views.follow import follow_toggle, FollowingPostListView
from webapp.views.post import profile_view

urlpatterns = [
    path('', ProfileView.as_view(), name='index'),
    path('<str:username>/', profile_view, name='profile'),
    path('post/create/', CreatePostView.as_view(), name='post_create'),
    path('user/<int:pk>/', UserProfileView.as_view(), name='user_profile'),
    path('user/<int:pk>/subscribe/', UserSubscribeView.as_view(), name='subscribe'),
    path('user/<str:username>/follow/', follow_toggle, name='follow_toggle'),
    path('following-posts/', FollowingPostListView.as_view(), name='following_posts'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.MEDIA_URL + 'uploads/', document_root=settings.MEDIA_ROOT + 'uploads/')
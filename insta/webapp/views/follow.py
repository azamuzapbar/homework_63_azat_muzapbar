from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth import get_user_model
from django.views.generic import ListView
from webapp.models import Post

User = get_user_model()

def follow_toggle(request, username):
    user = request.user
    account = get_object_or_404(User, username=username)
    if user in account.followers.all():
        account.followers.remove(user)
        user.profile.following.remove(account)
    else:
        account.followers.add(user)
        user.profile.following.add(account)
    return redirect('profile', username=username)


class FollowingPostListView(ListView):
    model = Post
    template_name = 'following_post_list.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        following = self.request.user. account.following.all()
        queryset = Post.objects.filter(author__in=following).order_by('-created_at')
        return queryset
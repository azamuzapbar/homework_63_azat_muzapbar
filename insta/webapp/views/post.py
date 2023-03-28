from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, get_object_or_404, render
from django.views.generic.edit import CreateView
from webapp.models import Post
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from accounts.models import Account

@login_required
def profile_view(request, username):
    account = get_object_or_404(User, username=username)
    posts = Post.objects.filter(author=account).order_by('-created_at')
    return render(request, 'profile.html', {'account': account, 'posts': posts})

class CreatePostView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['description', 'image']
    template_name = 'create_post.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.likes_count = 0
        form.instance.comments_count = 0
        return super().form_valid(form)



class UserProfileView(LoginRequiredMixin, DetailView):
    model = Account
    template_name = 'user_profile.html'

class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = Account
    fields = ['first_name', 'last_name', 'email', 'avatar', 'info']
    template_name = 'user_update.html'
    success_url = reverse_lazy('profile')

class UserSubscribeView(LoginRequiredMixin, DetailView):
    model = Account
    template_name = 'user_subscribe.html'

    def post(self, request, *args, **kwargs):
        subscriber = self.request.user.account
        user = self.get_object()
        subscriber.subscriptions.add(user)
        user.subscribers.add(subscriber)
        return redirect('user_profile', pk=user.pk)
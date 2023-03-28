from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q

from webapp.models import Post,Comment
from accounts.models import Account
from webapp.forms import CommentForm



class ProfileView(LoginRequiredMixin, ListView):
    model = Account
    template_name = 'index.html'
    context_object_name = 'account'
    paginate_by = 10

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        subscriptions = user.subscriptions.all()
        posts = Post.objects.filter(Q(author__in=subscriptions) | Q(author=user)).order_by('-created_at')
        comments = Comment.objects.all()
        context['posts'] = posts
        context['comment_form'] = CommentForm()
        context['comments'] = comments
        return context


def search_profiles(request):
    search_value = request.GET.get('search', None)
    accounts = Account.objects.filter(Q(username__icontains=search_value) |
                                       Q(email__icontains=search_value) |
                                       Q(first_name__icontains=search_value),
                                       is_deleted=False).exclude(pk=request.user.pk)
    context = {'accounts': accounts, 'search_value': search_value}
    return render(request, 'search.html', context)
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from accounts.views import LoginView, logout_view, RegisterView, ProfileView, UserChangeView

urlpatterns =[
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/<int:pk>', ProfileView.as_view(), name='profile'),
    path('profile/<int:pk>/change', UserChangeView.as_view(), name='change')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
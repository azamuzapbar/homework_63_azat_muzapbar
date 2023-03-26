from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models
from accounts.managers import UserManager

GENDER = \
    (('male', 'Мужской'),
     ('female', 'Женский'))


class Account(AbstractUser):
    email = models.EmailField(verbose_name='Электронная почта', unique=True, blank=True)

    avatar = models.ImageField(
        null=True,
        blank=True,
        upload_to='user_pic',
        verbose_name='Аватар'
    )
    info = models.TextField(verbose_name='Личная информация', blank=True, null=True)
    phone = models.CharField(verbose_name='Номер телефона', null=True, blank=True, unique=True,max_length=500)
    gender = models.TextField(verbose_name='Пол', choices=GENDER, null=False, blank=False)
    birth_date = models.DateField(
        null=True,
        blank=True,
        verbose_name='Дата рождения'
    )
    liked_posts = models.ManyToManyField(
        verbose_name='Понравившиеся публикации',
        to='webapp.Post',
        related_name='user_likes')
    subscriptions = models.ManyToManyField(
        verbose_name='Подписки',
        to='accounts.Account',
        related_name='subscribers')
    commented_posts = models.ManyToManyField(
        verbose_name='Прокомментированные публикации',
        to='webapp.Post',
        related_name='user_comments'
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    object = UserManager()

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

import enum
from typing import Any

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.core.handlers.wsgi import WSGIRequest
from timestamps.models import Timestampable
from django.db import models
from django.conf import settings
from django.dispatch import receiver


class AuthJournalEventType(models.TextChoices):
    LOGIN = "Авторизация"
    LOGOUT = "Выход"
    LOGIN_FAILED = "Авторизация с ошибкой"


class AuthJournal(Timestampable):
    event_type = models.CharField(
        max_length=50,
        choices=AuthJournalEventType,
        default=AuthJournalEventType.LOGIN_FAILED,
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, null=True)
    comment = models.CharField(null=True)
    ip = models.GenericIPAddressField(null=True)

    def __str__(self) -> str:
        log_record_text = f"{self.created_at} | Тип действия {self.event_type}"
        if self.user:
            log_record_text += f" | Пользователь {self.user.username}"
        log_record_text += f" | IP {self.ip} | Информация {self.comment}"

        return log_record_text


@receiver(user_logged_in)
def user_logged_in_callback(
    sender: Any,
    request: WSGIRequest,
    user: AbstractUser,
    **kwargs: Any,
) -> None:
    AuthJournal.objects.create(
        event_type=AuthJournalEventType.LOGIN,
        user=user,
        ip=request.META.get('REMOTE_ADDR'),
        comment="Вход успешен",
    )


@receiver(user_logged_out)
def user_logged_out_callback(
    sender: Any,
    request: WSGIRequest,
    user: AbstractUser,
    **kwargs: Any,
) -> None:
    AuthJournal.objects.create(
        event_type=AuthJournalEventType.LOGOUT,
        user=user,
        ip=request.META.get('REMOTE_ADDR'),
        comment="Выход успешен",
    )


@receiver(user_login_failed)
def user_login_failed_callback(
    sender: Any,
    credentials: dict,
    **kwargs: Any,
) -> None:
    AuthJournal.objects.create(
        event_type=AuthJournalEventType.LOGIN_FAILED,
        comment=f"username {credentials.get('username', None)}",
    )

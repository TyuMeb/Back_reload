from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.db import models
from rest_framework.exceptions import ValidationError


class UserAccountManager(BaseUserManager):
    def create(self, email, name, person_telephone, surname=None, password=None):
        if not email:
            raise ValidationError({"error": "Не указана почта"})

        if not name or len(name) <= 2 or len(name) >= 50:
            raise ValidationError({"error": "Укажите корректное имя"})

        if person_telephone[0:2] != '+7' or len(person_telephone) != 12 or person_telephone[1:].isdigit() is False:
            raise ValidationError({"error": "Телефон должен начинаться с +7 и иметь 12 символов(цифры)."})

        email = self.normalize_email(email)
        user = self.model(
            email=email, name=name, person_telephone=person_telephone, surname=surname
        )

        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, name, person_telephone, surname, password=None):
        email = self.normalize_email(email)
        user = self.model(
            email=email, name=name, person_telephone=person_telephone, surname=surname
        )
        user.set_password(password)
        user.save()

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save(using=self._db)
        return user


class UserAccount(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_partner = models.BooleanField(default=False)
    person_rating = models.IntegerField("Рейтинг клиента", blank=True, null=True)
    person_created = models.DateTimeField("Дата создания аккаунта", auto_now=True)
    person_telephone = models.CharField(
        "Номер телефона", max_length=20, blank=True, null=True
    )
    person_address = models.CharField("Адрес", max_length=200, blank=True, null=True)

    objects = UserAccountManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name", "person_telephone"]

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Пользователи"
        verbose_name_plural = "Пользователи"


class SellerData(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    user_account_id = models.ForeignKey(
        UserAccount, on_delete=models.CASCADE, null=True
    )
    seller_activity = models.BooleanField("Активен / Не активен", default=False)
    seller_name_company = models.CharField("Имя компании", max_length=100, blank=True)
    seller_date = models.DateTimeField("Дата создания аккаунта продавца", auto_now=True)
    seller_telephone = models.CharField("Телефон компании", max_length=20, blank=True)
    seller_requisites = models.CharField(
        "Реквизиты компании", max_length=100, blank=True
    )
    seller_type_activity = models.CharField(
        "Болванка тут должна быть связь с видом деятельности",
        max_length=100,
        blank=True,
    )

    class Meta:
        verbose_name = "Продавцы"
        verbose_name_plural = "Продавцы"


class CooperationOffer(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    user_account_id = models.ForeignKey(
        UserAccount, on_delete=models.CASCADE, null=True
    )
    text = models.CharField(
        "Запрос от пользователя", max_length=20, blank=True, null=True
    )
    created = models.DateTimeField("Дата создания обращения", auto_now=True)

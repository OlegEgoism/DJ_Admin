from django.db import models


class UserInfo(models.Model):
    name = models.CharField(verbose_name="Имя", max_length=200, default='User')
    year = models.PositiveIntegerField(verbose_name="Возраст")
    address = models.CharField(verbose_name="Адресс", max_length=200, blank=True, null=True)
    skill = models.CharField(verbose_name="Умения", max_length=200, blank=True, null=True)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = "name",

    def __str__(self):
        return self.name

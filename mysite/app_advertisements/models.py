from django.db import models
from django.contrib import admin
from django.utils.html import format_html
# Create your models here.


class Advertisement(models.Model):

    title = models.CharField("заголовок", max_length=60)
    description = models.TextField("описание")
    price = models.DecimalField("цена", max_digits=10, decimal_places=2)

    updated_at = models.DateTimeField("дата обновления", auto_now=True)
    created_at = models.DateTimeField("дата публикации", auto_now_add=True)
    is_auction = models.BooleanField("уместен ли торг", help_text="отметьте, если торг по бъявлению уместен")

    @admin.display(description="Дата публикации")
    def created_date(self):
        from django.utils import timezone
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime("%H:%M:%S")
            return format_html(
                "<span>Сегодня в {}</span>", created_time
            )
        else:
            return self.created_at.strftime("%d.%m.%Y - %H:%M")

    class Meta:
        db_table = "Advertisements"

    def __str__(self):
        return f"Advertisement(id={self.id}, title={self.title}, is_auction={self.is_auction})"
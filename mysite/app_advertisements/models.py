from django.db import models

# Create your models here.


class Advertisement(models.Model):

    title = models.CharField("заголовок", max_length=60)
    description = models.TextField("описание")
    price = models.DecimalField("цена", max_digits=10, decimal_places=2)

    updated_at = models.DateTimeField("дата обновления", auto_now=True)
    created_at = models.DateTimeField("дата публикации", auto_now_add=True)
    is_auction = models.BooleanField("уместен ли торг", help_text="отметьте, если торг по бъявлению уместен")

    class Meta:
        db_table = "Advertisements"

    def __str__(self):
        return f"Advertisement(id={self.id}, title={self.title}, is_auction={self.is_auction})"
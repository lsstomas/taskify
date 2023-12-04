from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    user = models.ForeignKey(
        blank=True,
        null=True,
        to=User,
        on_delete=models.CASCADE,
        related_name="categories",
    )

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self) -> str:
        return self.name

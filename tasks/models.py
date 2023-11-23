from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=7, default="#FFFFFF")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="categories")

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self) -> str:
        return self.name


class Task(models.Model):
    PRIORITY_CHOICES = [
        ("B", "Baixa"),
        ("M", "Média"),
        ("A", "Alta"),
    ]

    STATUS_CHOICES = [
        ("N", "Não Iniciado"),
        ("P", "Em Progresso"),
        ("R", "Em Revisão"),
        ("C", "Concluído"),
        ("D", "Desativado"),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    due_date = models.DateTimeField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES, default="M")
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasks")
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default="P")

    class Meta:
        verbose_name = "Tarefa"
        verbose_name_plural = "Tarefas"

    def __str__(self):
        return self.title

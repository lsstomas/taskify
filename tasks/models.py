from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from categories.models import Category


class Task(models.Model):
    PRIORITY_CHOICES = [
        ("B", "Baixa"),
        ("M", "Média"),
        ("A", "Alta"),
    ]

    STATUS_CHOICES = [
        ("N", "Não Iniciado"),
        ("P", "Em Progresso"),
        ("C", "Concluído"),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    due_date = models.DateTimeField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES, default="M")
    conclution_date = models.DateTimeField(null=True, blank=True)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasks")
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default="P")

    def formatted_due_date(self):
        return self.due_date.strftime("%d/%m/%y %Hh%M")

    class Meta:
        verbose_name = "Tarefa"
        verbose_name_plural = "Tarefas"

    def __str__(self):
        return self.title

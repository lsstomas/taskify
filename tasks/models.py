from django.db import models
from django.forms import ValidationError
from django.utils import timezone
from django.contrib.auth.models import User
from categories.models import Category
from django.contrib import messages
from datetime import timedelta


class Task(models.Model):
    NOTIFICATION_CHOICES = [
        (1, "1 minuto"),
        (5, "5 minutos"),
        (15, "15 minutos"),
        (30, "30 minutos"),
        (60, "1 hora"),
        (180, "3 horas"),
        (1440, "1 dia"),
        (10080, "1 semana"),
    ]

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
    reminder_sent = models.BooleanField(default=False)
    notification_time = models.IntegerField(choices=NOTIFICATION_CHOICES, default=1440)

    def formatted_due_date(self):
        self.due_date = self.due_date - timedelta(hours=3)
        return self.due_date.strftime("%d/%m/%y %Hh%M")

    class Meta:
        verbose_name = "Tarefa"
        verbose_name_plural = "Tarefas"

    def __str__(self):
        return self.title

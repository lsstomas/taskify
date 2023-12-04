from django.core.management.base import BaseCommand
from django.utils import timezone
from django.core.mail import send_mail
from tasks.models import Task
from datetime import timedelta
from django.conf import settings
import logging


class Command(BaseCommand):
    help = "Envia lembretes de tarefas próximas do prazo"

    def handle(self, *args, **kwargs):
        logger = logging.getLogger(__name__)

        now = timezone.now()
        tasks = Task.objects.filter(reminder_sent=False)

        for task in tasks:
            reminder_time = task.due_date - timedelta(hours=task.notification_time)

            if now >= reminder_time:
                logger.info(f"Enviando lembrete para a tarefa {task.title}")

                send_mail(
                    subject=f"Lembrete de Tarefa: {task.title}",
                    message=f'Olá, a tarefa "{task.title}" está próxima do prazo. Não se esqueça de completá-la!',
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[task.user.email],
                    fail_silently=False,
                )

                # Marca a tarefa como lembrete enviado
                task.reminder_sent = True
                task.save()

        self.stdout.write(
            self.style.SUCCESS(f"Lembretes de tarefa enviados com sucesso.")
        )

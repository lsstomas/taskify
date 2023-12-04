from django import forms
from .models import Task, Category
from datetime import timedelta
from django.utils import timezone


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            "title",
            "description",
            "due_date",
            "notification_time",
            "priority",
            "category",
            "status",
        ]

    widgets = {
        "notification_time": forms.Select(choices=Task.NOTIFICATION_CHOICES),
    }

    def clean(self):
        cleaned_data = super().clean()
        due_date = cleaned_data.get("due_date")
        notification_time = cleaned_data.get("notification_time")

        if due_date and notification_time:
            if due_date - timezone.now() < timedelta(minutes=notification_time):
                self.add_error(
                    "notification_time",
                    "O tempo de notificação deve ser menor que o tempo restante até o prazo.",
                )

    def __init__(self, user=None, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        if user:
            self.fields["category"].queryset = Category.objects.filter(user=user)

# Generated by Django 4.2.7 on 2023-11-27 17:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tasks", "0002_alter_task_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="status",
            field=models.CharField(
                choices=[
                    ("N", "Não Iniciado"),
                    ("P", "Em Progresso"),
                    ("C", "Concluído"),
                ],
                default="P",
                max_length=1,
            ),
        ),
    ]

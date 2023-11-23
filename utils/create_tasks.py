import os
import sys
from datetime import datetime
from pathlib import Path
from random import choice

import django
from django.conf import settings

DJANGO_BASE_DIR = Path(__file__).parent.parent
NUMBER_OF_OBJECTS = 150

sys.path.append(str(DJANGO_BASE_DIR))
os.environ["DJANGO_SETTINGS_MODULE"] = "taskify.settings"
settings.USE_TZ = False

django.setup()

if __name__ == "__main__":
    import faker

    from tasks.models import Category, Task
    from django.contrib.auth.models import User

    Task.objects.all().delete()
    Category.objects.all().delete()

    fake = faker.Faker("pt-BR")
    categories = ["Metas", "Trabalho", "Pessoal"]

    django_tasks = []
    django_users = [User.objects.get(username="luis")]

    django_categories = [
        Category(name=name, user=choice(django_users)) for name in categories
    ]

    for category in django_categories:
        category.save()

    for _ in range(NUMBER_OF_OBJECTS):
        title = fake.sentence()
        description = fake.text(max_nb_chars=100)
        due_date: datetime = fake.date_time_this_year()
        created_at: datetime = fake.date_time_this_year()
        priority = choice(["B", "M", "A"])
        category = choice(django_categories)
        status = choice(["N", "P", "R", "C"])
        user = choice(django_users)

        django_tasks.append(
            Task(
                title=title,
                description=description,
                due_date=due_date,
                created_at=created_at,
                priority=priority,
                category=category,
                status=status,
                user=user,
            )
        )

    if len(django_tasks) > 0:
        Task.objects.bulk_create(django_tasks)

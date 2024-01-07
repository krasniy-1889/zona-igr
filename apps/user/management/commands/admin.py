import os

from django.contrib.auth import get_user_model
from django.core.management import BaseCommand
from dotenv import load_dotenv

load_dotenv()


class Command(BaseCommand):
    help = "Create an admin user"

    def handle(self, *args, **options):
        username = os.environ.get("ADMIN_USERNAME", "admin")
        email = os.environ.get("ADMIN_EMAIL", "admin@localhost")
        password = os.environ.get("ADMIN_PASSWORD", "admin")
        get_user_model().objects.create_superuser(username, email, password)
        self.stdout.write(self.style.SUCCESS("Admin user created successfully!"))

from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User

class Command(BaseCommand):

    def handle(self, *args, **options):
        if not User.objects.filter(username="bryan").exists():
            User.objects.create_superuser("bryan", "brymurph@gmail.com", "L1quidpaper")
            self.stdout.write(self.style.SUCCESS('Successfully created new super user'))
from django.contrib.auth.models import User
from myApp.models import Profile  
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Create profiles for users without profiles'

    def handle(self, *args, **options):
        for user in User.objects.filter(profile__isnull=True):
            profile = Profile(user=user)
            profile.save()
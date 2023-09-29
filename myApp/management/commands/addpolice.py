from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group
from myApp.models import PoliceOfficer

class Command(BaseCommand):
    help = 'Assign all PoliceOfficers to the PoliceOfficers group'

    def handle(self, *args, **kwargs):
        try:
            police_officers_group = Group.objects.get(name='PoliceOfficers')
        except Group.DoesNotExist:
            # Handle the case where the group doesn't exist
            self.stdout.write(self.style.ERROR('The "PoliceOfficers" group does not exist.'))
            return

        police_officers = PoliceOfficer.objects.all()

        for police_officer in police_officers:
            police_officer.user.groups.add(police_officers_group)
            self.stdout.write(self.style.SUCCESS(f'Assigned {police_officer.name} to the "PoliceOfficers" group.'))

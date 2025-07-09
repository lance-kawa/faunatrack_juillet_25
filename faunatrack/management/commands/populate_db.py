from django.core.management.base import BaseCommand

from faunatrack.models import FaunatrackUser, Location, Observation, Project, ProjectUserAccess, Species
from django.utils import timezone
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = "Populate the database with sample data"


    def handle(self, *args, **options):
        for i in range(1,30):
            espece, _ = Species.objects.get_or_create(name=f"Espece {i}", defaults={"at_risk": True})
            project, _ = Project.objects.get_or_create(title=f"Project {i}")
            location, _ = Location.objects.get_or_create(name=f"Location {i}", defaults={"lattitude":-45+i, "longitude":12+i})
            quantity = i
            now = timezone.now()
            date_observation = now + timezone.timedelta(days=i)
            django_user, _ = User.objects.get_or_create(email=f"email@{i}.com", username=f"user{i}")
            user, _ = FaunatrackUser.objects.get_or_create(user=django_user)
            user_access, _ = ProjectUserAccess.objects.get_or_create(project=project, user=user)
            Observation.objects.create(
                species=espece,
                quantity=quantity,
                date_observation=date_observation,
                location=location,
                project=project
            
            )


        
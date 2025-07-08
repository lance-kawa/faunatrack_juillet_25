from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.db.models import QuerySet
import uuid

# 2 approche 

# Courante, Traditionnelle 
# Je fais ma vie en local mabranche/feature
# Je push mon code
# Je règle avec mes collègues les conflits sur les migrations lors du merge vers main


# Nouvelle approche 
# Je fais ma vie en local sur mabranche/feature
# Je ne crée JAMAIS de migrations
# Je pousse sur une branche intermédiaire epic/features
# sur epic/features => makemigrations en équipe


# Attention avec Sqlite3, les contraintes ne sont pas appliqués sur la BDD (il faut passer par Django)

class BaseModel(models.Model):

    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True # Modèle Abstrait, ne crée pas de tables en bdd
        


class Species(BaseModel):
    # name = models.CharField(max_length=255, null=True, blank=True, unique=True, default="", verbose_name=_("name"))
    name = models.CharField(max_length=255, unique=True, verbose_name=_("name"))
    at_risk = models.BooleanField(default=False)

    class Meta: # Modifier le nom de la table, la pluralisation, les index, les constraints
        verbose_name = _("Species")
        verbose_name_plural = _("Species")


    def __str__(self):
        return self.name
    

class ObservationManager(models.Manager):   

    def in_public_project(self):
        return self.get_queryset().filter(project__is_public=True)


class ObservationProjetManager(models.Manager):   

    def public(self):
        return self.get_queryset().filter(project__is_public=True)
    
    def private(self):
        return self.get_queryset().filter(project__is_public=False)
        
class Observation(BaseModel):
    objects = ObservationManager() 
    projets = ObservationProjetManager()
    
    species: Species = models.ForeignKey(Species, on_delete=models.PROTECT, related_name="observations") # related_name !!!
    date_observation = models.DateTimeField()
    notes = models.TextField(null=True, blank=True) # Microsoft berk
    quantity = models.PositiveIntegerField(default=1, blank=True)
    project = models.ForeignKey('faunatrack.Project', on_delete=models.PROTECT, related_name="observations")
    location = models.ForeignKey('faunatrack.Location', on_delete=models.PROTECT, related_name="observations") 


    def __str__(self):
        return f"{self.species.name} (vu: {self.quantity}) - {self.location}"

    class Meta:
        # ordering = ["-date_observation"]
        indexes = [
            models.Index(fields=["species", "location", "date_observation"], name="observation_index"),
        ]

        unique_together = ["date_observation", "species", "location"] # métiers ! 
        verbose_name = _("Observation")
        verbose_name_plural = _("Observations")

class ObservationImage(BaseModel):
    observation = models.ForeignKey(Observation, null=True, on_delete=models.SET_NULL, related_name="images") # PO pas content mais formateur content
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    
    def __str__(self):
        return self.observation

    class Meta:
        verbose_name = _("ObservationImage")
        verbose_name_plural = _("ObservationImages")


class Project(BaseModel):

    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    is_public = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} ({self.is_public})"
    

    class Meta:
        verbose_name = _("Project")
        verbose_name_plural = _("Projects")

    observations : QuerySet[Observation] # On peut "typé" la relation inverssé pour aider notre IDE


class Location(BaseModel):
    name = models.CharField(max_length=255, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    lattitude = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Location")
        verbose_name_plural = _("Locations")

class ProjectUserAccess(BaseModel):
    class RolesTextChoices(models.TextChoices): # Liste énuméré
        # MON_CODE = ("bdd", "FrontendUser")
        ADMIN = ("admin", _("Admin"))
        SPECTATOR = ("spectator", _("Spectator"))
        CONTRIBUTOR = ("contributor", _("Contributor"))


    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="members")
    user = models.ForeignKey("faunatrack.FaunatrackUser", on_delete=models.CASCADE, related_name="project_access")
    roles = models.CharField(default=RolesTextChoices.CONTRIBUTOR, max_length=255, choices=RolesTextChoices.choices)

    class Meta:
        verbose_name = _("ProjectUserAccess")
        verbose_name_plural = _("ProjectUserAccesses")

    # def to_gmaps_name(self):
        # if self.lattitude and self.longitude:
            # self.name = call_api()
        # self.save()


class FaunatrackUser(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, related_name="faunatrack_user")


    class Meta:
        verbose_name = _("FaunatrackUser")
        verbose_name_plural = _("FaunatrackUsers")


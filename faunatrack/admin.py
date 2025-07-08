from django.contrib import admin
from django.db.models import QuerySet
from faunatrack.models import Species, Observation, ObservationImage, Project, ProjectUserAccess, Location, FaunatrackUser

# Register your models here.
@admin.register(Species)
class SpeciesAdmin(admin.ModelAdmin):
    readonly_fields = ["at_risk"]



@admin.register(Observation)
class ObservationAdmin(admin.ModelAdmin):

    list_display = ["__str__", 'species', 'projet', 'quantity', 'projet__title']

    list_filter = ["projet", "species__name"]
    search_fields = ["projet__title", "species__name"]
    search_help_text = "Bonjour"



@admin.register(ObservationImage)
class ObservationImageAdmin(admin.ModelAdmin):
    pass


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ["__str__"]
 
    
    actions = ["toogle_public"]

    def toogle_public(self, request, queryset: QuerySet[Project]):
        for project in queryset:
            project.is_public = not project.is_public
            project.save()


@admin.register(ProjectUserAccess)
class ProjectUserAccessAdmin(admin.ModelAdmin):
    pass

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    pass

@admin.register(FaunatrackUser)
class FaunatrackUserAdmin(admin.ModelAdmin):
    pass
    
   


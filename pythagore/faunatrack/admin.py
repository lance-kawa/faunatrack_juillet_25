from django.contrib import admin
from django.db.models import QuerySet
from faunatrack.models import Species, Observation, ObservationImage, Project, ProjectUserAccess, Location, FaunatrackUser

from import_export.admin import ImportExportModelAdmin
from import_export import resources


class ObservationResource(resources.ModelResource):
    class Meta:
        model = Observation
        


class ObservationInline(admin.TabularInline):
    model = Observation
    extra = 1

# Register your models here.
@admin.register(Species)
class SpeciesAdmin(admin.ModelAdmin):
    list_display = ["__str__", "at_risk"]
    readonly_fields = ["at_risk"]
    list_editable = ["at_risk"]

    inlines = [ObservationInline]


@admin.register(Observation)
class ObservationAdmin(ImportExportModelAdmin):

    list_display = ["__str__", 'species', 'project', 'quantity', 'project__title']

    list_filter = ["project", "species__name"]
    search_fields = ["project__title", "species__name"]
    search_help_text = "Bonjour"
    ordering = ["-date_observation"]

    resource_classes = [ObservationResource]



@admin.register(ObservationImage)
class ObservationImageAdmin(admin.ModelAdmin):
    pass




@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ["__str__", 'slug']
    readonly_fields = ["slug"]
    
    actions = ["toogle_public"]
    inlines = [ObservationInline]

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
    
   


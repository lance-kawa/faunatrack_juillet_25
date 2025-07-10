from django.contrib.auth.models import User
from rest_framework import serializers

from faunatrack.models import Location, Observation, Project, Species


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url',  'username', 'email', 'groups'] # __all__
        # exclude 


class SpeciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Species
        fields = '__all__'



    


class LocationSerializer(serializers.ModelSerializer):      
    class Meta:
        model = Location
        fields = '__all__' 


class LocationForObservationWithoutLatitudeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'name']




class ProjectObservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class ObservationSerializer(serializers.ModelSerializer):
    project_nb_obs = serializers.SerializerMethodField()
    species_name = serializers.CharField(source="species.name", read_only=True)
    project_title = serializers.CharField(source="project.title", read_only=True)
    species = SpeciesSerializer()
    project = ProjectObservationSerializer()
    location = LocationForObservationWithoutLatitudeSerializer()


    class Meta:
        model = Observation
        fields = ['id', 'project_nb_obs', 'species_name', 'project_title', 'species', 'project', 'location']
        # exclude = ["id"]
        # exclude 
    
    # get_ + nom du champ
    def get_project_nb_obs(self, obj: Observation):
        return obj.project.observations.count()
    

class ObservationCreateSerializer(ObservationSerializer):
    class Meta:
        model = Observation
        fields = ['species', 'notes', 'quantity', 'location', 'project']

    
    # def to_internal_value(self, data):

    #     return data
    
    # def validate_notes(self):
    #     notes = self.cleaned_data.get('notes', None)
    #     if "pas beau" in notes:
    #         raise forms.ValidationError("Votre observation doit être plus belle que ça voyons !")
    #     return notes
    
    # def validate(self, data):
    #     return data

class ProjectSerializer(serializers.ModelSerializer):
    observations = ObservationSerializer(many=True)
    class Meta:
        model = Project
        fields = '__all__'
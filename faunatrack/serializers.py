from django.contrib.auth.models import User
from rest_framework import serializers

from faunatrack.models import Observation


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url',  'username', 'email', 'groups'] # __all__
        # exclude 






class ObservationSerializer(serializers.ModelSerializer):
    project_nb_obs = serializers.SerializerMethodField()
    species_name = serializers.CharField(source="species.name")


    class Meta:
        model = Observation
        fields = ['id', 'project_nb_obs', 'species_name']
        # exclude = ["id"]
        # exclude 
    
    def get_project_nb_obs(self, obj: Observation):
        return obj.project.observations.count()
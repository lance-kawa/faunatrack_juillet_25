from django.contrib.auth.models import  User
from rest_framework import permissions, viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from faunatrack.models import Observation, Species
from faunatrack.serializers import ObservationCreateSerializer, ObservationSerializer, UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = []
    # authentication_classes = [BasicAuthentication]


class ExampleView(APIView):

    def get(self, request, format=None):
        content = {
            'user': str(request.user),  # `django.contrib.auth.User` instance.
            'auth': str(request.auth),  # None
        }
        return Response(content)
    

class ObservationViewSet(viewsets.ModelViewSet):
    # permission_classes = []
    queryset = Observation.objects.all()

    def get_serializer_class(self):
        if self.action == 'create': #list #retrieve #update #destroy #partial_update
            return ObservationCreateSerializer
        return ObservationSerializer

    # je me connexte avec user password 
    # => Je réupère acces + resfresh 
    # je les met dans le local storage
        # Je query l'api avec access-token
        # Si erreur (403?)
        # Je query l'api avec refresh-token /refresh
        # Je récupère un nouveau access-token
        # loop
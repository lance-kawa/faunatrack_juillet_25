"""
URL configuration for pythagore project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include, path
from faunatrack.api import UserViewSet, ExampleView, ObservationViewSet, ProjectViewSet
from faunatrack.views import home, mes_projets, ObservationCreate, ObservationList, ObservationDelete
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = routers.DefaultRouter()
router.register("users", UserViewSet, basename="user")
router.register("observations", ObservationViewSet, basename="observation")
router.register("projects", ProjectViewSet, basename="projects")

# router.register("observations", UserViewSet, basename="user")

urlpatterns = [
    path("", home, name="home"),
    path("projets/", mes_projets, name="list_projects"),
    path("projets/<str:slug>/", mes_projets, name="mes_projets"),
    path("observations/create/", ObservationCreate.as_view(), name="create_observation"),
    path("observations/", ObservationList.as_view(), name="list_obs"),
    path("observations/<int:pk>/delete/", ObservationDelete.as_view(), name="delete_obs"),
    path('api/', include(router.urls)),
    path('api/example/', ExampleView.as_view(), name='example'),
    path("api/auth/token/", TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path("species/", SpeciesList.as_view(), name="list_species"),
]




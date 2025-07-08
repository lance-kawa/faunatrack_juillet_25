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
from django.urls import path
from faunatrack.views import home, mes_projets, ObservationCreate, ObservationList, ObservationDelete

urlpatterns = [
    path("", home, name="home"),
    path("projets/", mes_projets, name="mes_projets"),
    path("observations/create/", ObservationCreate.as_view(), name="create_observation"),
    path("observations/", ObservationList.as_view(), name="list_obs"),
    path("observations/<int:pk>/delete/", ObservationDelete.as_view(), name="delete_obs"),
]

from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils import timezone
from faunatrack.forms import ObservationForm
from faunatrack.models import FaunatrackUser, Location, Observation, Project, ProjectUserAccess, Species
from django.db.models import QuerySet
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.contrib.auth.models import User

def home(request):
    return render(request, "home.html", context={
        "today": timezone.now()
    })

def mes_projets(request):
    user: User = request.user
    if not user.is_authenticated or not user.faunatrack_user:
        return redirect('login')
    
    # user_accesses = ProjectUserAccess.objects.filter(user=user.faunatrack_user, roles=ProjectUserAccess.RolesTextChoices.ADMIN)
    # projects_ids = user_accesses.values_list("project", flat=True)
    # print(projects_ids)
    # projects = Project.objects.filter(id__in=projects_ids)

    projects = Project.objects.filter(members__user=user.faunatrack_user, members__roles=ProjectUserAccess.RolesTextChoices.ADMIN)
    # print(user.faunatrack_user.project_access.filter(roles=ProjectUserAccess.RolesTextChoices.ADMIN))

    return render(request, "mes_projets.html", context={
        "projet_list": projects
    })
   


class AuthenticateMixin(LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin ):
    def test_func(self):
        # Test fonctionnel
        # Je ne peux créer des obs que si il existe déjà des obs sur les projets auquel j'appartiens
        user = self.request.user
        test = Observation.objects.filter(project__members__user=user.faunatrack_user, project__members__roles=ProjectUserAccess.RolesTextChoices.ADMIN).exists()
        return test



class ObservationCreate(AuthenticateMixin, CreateView):
    model = Observation
    template_name = "observations/create.html"
    success_url = reverse_lazy("home")
    form_class = ObservationForm  
    # permissions = ["faunatrack.add_observation"] #app_label.add/change/delete/view_{model_name}
    permission_required = "faunatrack.add_observation"


class ObservationDelete(DeleteView):
    model = Observation
    template_name = "observations/delete.html"
    success_url = reverse_lazy("home")

class ObservationList(ListView):
    model = Observation
    queryset = Observation.objects.filter(species__at_risk=True)
    template_name = "observations/list.html"


class ProjetList(ListView):
    model = Project
    queryset = Project.objects.all()
    template_name = "project/list.html"

# from django.db import models
# class SpeciesList(View):
   

#     def get(self, *args):
#         return render(self.request, 'species/list.html', context={
#             'object_list': self.get_queryset()
#         } )


#     def get_queryset(self):
#         faunatrack_user = self.request.user.faunatrack_user
#         projects = Project.objects.filter(members__user=faunatrack_user)

#         return  Species.objects.filter(observations__project__in=projects).distinct()

        # projects_ids = Project.objects.filter(members__user=faunatrack_user).values_list('id', flat=True)
        # species_qs = Species.objects.filter(observations__project_id__in=projects_ids).distinct()
        # species_qs = Species.objects.filter(observations__project__id__in=projects_ids).distinct()
        # loc_list = []
        # for species in species_qs:
        #     obs_qs: QuerySet[Observation]  = species.observations.all()
        #     for obs in obs_qs:
        #         location: Location = obs.location
        #         total = Observation.objects.filter(location=location).aggregate(total=models.Sum('quantity'))['total']
        #         loc_list.append(location)
                
        # loc_list = set(loc_list)

        

        # POUR chaque species :
        # Récupérer ses observations, l'emplacement de ces observations
        # Compter la somme des quantités observé sur un emplacement donné 
        # retourner le plus haut


    # bad pattern
    # if condition:
    #     return None
    # return list
    
    # good pattern
    # if condition:
    #     raise Exception
    # return list
    


 # print(user)
    # if not user.is_authenticated:
    #     return redirect("login")
    # # ORM = SDK de votre bdd 
    # # Un queryset est un built in list python ET un QuerySet, on peut utiliser les méthodes de l'ORM ou des listes 
    # projets: QuerySet[Project] = Project.objects.all() # Les QS sont lazy evaluated, la requête SQL est effectué seulement lorsque django a besoin de la donnée
    # projets = projets.filter(observations__species__at_risk=True).order_by('-created_at') # convention order_by('-created_at').first() à la place de  order_by('created_at').last()
    # projets_list_id = projets.values_list('id', flat=True)

    # # obs_public = Observation.objects.filter(species__name="Ours").public()

    # # python manage.py shell_plus --print-sql
    # # lance un shell et print les requetes sql de l'ORM, pratique pour inspecter perfs (nécessite django_extensions)
    # # https://docs.djangoproject.com/fr/5.2/ref/models/querysets/#select-related 
    # # https://docs.djangoproject.com/fr/5.2/ref/models/querysets/#select-for-update
    # # A LIRE, docs perfs ORM



    # # https://docs.djangoproject.com/fr/5.2/ref/models/querysets/#methods-that-do-not-return-querysets
    # # create, exists
    # # https://docs.djangoproject.com/fr/5.2/ref/models/querysets/#field-lookups
    # # lookups
    # projet = Project.objects.create(title="test", description="test")

    # projet.title = "test2"
    # projet.save()

    # if Project.objects.filter(title="test").exists():
    #     print("yes")
    


    # # Exemple pour récupérer un seul objet 
    # # obs_id = 1
    # # try:    
    # #     Observation.objects.get(id=obs_id)
    # # except Observation.DoesNotExist:
    # #     return HttpResponse('404!')
    # # get_object_or_404(Observation, id=obs_id)    
    # # obs = Observation.objects.filter(id=obs_id).first() None if not exists
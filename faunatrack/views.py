from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils import timezone
from faunatrack.forms import ObservationForm
from faunatrack.models import Observation, Project
from django.db.models import QuerySet
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    return render(request, "home.html", context={
        "today": timezone.now()
    })

def mes_projets(request):
    user: User = request.user
    print(user)
    if not user.is_authenticated:
        return redirect("login")
    # ORM = SDK de votre bdd 
    # Un queryset est un built in list python ET un QuerySet, on peut utiliser les méthodes de l'ORM ou des listes 
    projets: QuerySet[Project] = Project.objects.all() # Les QS sont lazy evaluated, la requête SQL est effectué seulement lorsque django a besoin de la donnée
    projets = projets.filter(observations__species__at_risk=True).order_by('-created_at') # convention order_by('-created_at').first() à la place de  order_by('created_at').last()
    projets_list_id = projets.values_list('id', flat=True)

    # obs_public = Observation.objects.filter(species__name="Ours").public()

    # python manage.py shell_plus --print-sql
    # lance un shell et print les requetes sql de l'ORM, pratique pour inspecter perfs (nécessite django_extensions)
    # https://docs.djangoproject.com/fr/5.2/ref/models/querysets/#select-related 
    # https://docs.djangoproject.com/fr/5.2/ref/models/querysets/#select-for-update
    # A LIRE, docs perfs ORM



    # https://docs.djangoproject.com/fr/5.2/ref/models/querysets/#methods-that-do-not-return-querysets
    # create, exists
    # https://docs.djangoproject.com/fr/5.2/ref/models/querysets/#field-lookups
    # lookups
    projet = Project.objects.create(title="test", description="test")

    projet.title = "test2"
    projet.save()

    if Project.objects.filter(title="test").exists():
        print("yes")
    


    # Exemple pour récupérer un seul objet 
    # obs_id = 1
    # try:    
    #     Observation.objects.get(id=obs_id)
    # except Observation.DoesNotExist:
    #     return HttpResponse('404!')
    # get_object_or_404(Observation, id=obs_id)    
    # obs = Observation.objects.filter(id=obs_id).first() None if not exists
    

    return render(request, "mes_projets.html", context={
        "projet_list": projets
    })




class ObservationCreate(CreateView):
    model = Observation
    template_name = "observations/create.html"
    success_url = reverse_lazy("home")
    form_class = ObservationForm  
    permissions = ["faunatrack.add_observation"] #app_label.add/change/delete/view_{model_name}


class ObservationDelete(DeleteView):
    model = Observation
    template_name = "observations/delete.html"
    success_url = reverse_lazy("home")

class ObservationList(ListView):
    model = Observation
    queryset = Observation.objects.filter(species__at_risk=True)
    template_name = "observations/list.html"


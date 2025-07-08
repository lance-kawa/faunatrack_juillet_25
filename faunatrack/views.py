from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.utils import timezone
from faunatrack.models import Observation, Project
from django.db.models import QuerySet


# Create your views here.
def home(request):
    return render(request, "home.html", context={
        "today": timezone.now()
    })

def mes_projets(request):
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

    if Project.objects.filter(title="test").exists():
        print("yes")
    

    print(projet.__dict__)

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



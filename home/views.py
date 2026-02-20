from django.shortcuts import render, redirect
from .forms import FireIncidentForm
from .models import FireIncident
from django.http import JsonResponse
from .models import Incendie
from .forms import CitoyenForm
from .models import Citoyen
 


# Création de la vue pour la page d'accueil
def index(request):
    return render(request, 'home/index.html')

# Nouvelle vue pour afficher consignes.html
def consignes(request):
    return render(request, 'home/consignes.html')

 # Nouvelle vue pour afficher consignes.html
def connexion(request):
    return render(request, 'home/connexion.html')

# Nouvelle vue pour afficher propos.html
def propos(request):
    return render(request, 'home/propos.html')

# Vue pour déclarer un incendie

def declare_fire(request):
    if request.method == 'POST':
        form = FireIncidentForm(request.POST)
        
        if form.is_valid():
            # Sauvegarder l'incident si le formulaire est valide
            form.save()
            return JsonResponse({'success': True, 'message': 'Incident déclaré avec succès'}, status=201)
        else:
            # Afficher les erreurs du formulaire
            return JsonResponse({'success': False, 'errors': form.errors}, status=400)

    else:
        form = FireIncidentForm()

    return render(request, 'home/index.html', {'form': form})

def incendies_api(request):
    incendies = Incendie.objects.all().values('latitude', 'longitude', 'description', 'type', 'severity')
    return JsonResponse({'incendies': list(incendies)})



#vue pour l'enregistrement d'un citoyen


def register(request):
    if request.method == "POST":
        form = CitoyenForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('connexion')  # Redirection vers la vue connexion
        else:
            print(f"Form errors: {form.errors}")  # Debugging des erreurs

    else:
        form = CitoyenForm()

    return render(request, 'home/connexion.html', {'form': form})

    
 



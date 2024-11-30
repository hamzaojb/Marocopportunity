from django.shortcuts import render
from .models import Publication, Categorie, Domaine

def liste_publications(request):
    categories = Categorie.objects.all()
    domaines = Domaine.objects.all()
    
    categorie_name = request.GET.get('categorie', '')
    domaine_name = request.GET.get('domaine', '')

    if categorie_name and domaine_name:
        publications = Publication.objects.filter(categorie__nom=categorie_name, domaine__nom=domaine_name).select_related('categorie', 'domaine').order_by('-date_publication')
    elif categorie_name:
        publications = Publication.objects.filter(categorie__nom=categorie_name).select_related('categorie').order_by('-date_publication')
    elif domaine_name:
        publications = Publication.objects.filter(domaine__nom=domaine_name).select_related('domaine').order_by('-date_publication')
    else:
        publications = Publication.objects.select_related('categorie', 'domaine').order_by('-date_publication')

    return render(request, 'blog/liste_publications.html', {'publications': publications, 'categories': categories, 'domaines': domaines})

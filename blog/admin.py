from django.contrib import admin
from .models import Publication, Categorie, Domaine

@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ('nom',)
    search_fields = ('nom',)

@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ('titre', 'categorie', 'date_publication', 'auteur')
    search_fields = ('titre', 'contenu')
    list_filter = ('categorie', 'date_publication')
    ordering = ('-date_publication',)
@admin.register(Domaine)
class DomaineAdmin(admin.ModelAdmin):
    list_display = ('nom',)

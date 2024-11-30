from django.db import models

class Categorie(models.Model):
    nom = models.CharField(max_length=200)  # Name of the category

    def __str__(self):
        return self.nom
class Domaine(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom

class Publication(models.Model):
    titre = models.CharField(max_length=200)  # Title of the publication
    image = models.ImageField(upload_to='publications_images/')  # Image for the publication
    contenu = models.TextField()  # Content of the publication
    lien = models.URLField(default='https://example.com')

    date_publication = models.DateTimeField(auto_now_add=True)  # Auto-set the publication date
    auteur = models.CharField(max_length=100, default='Anonymous')  # Author of the publication
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)  # Category relationship
    domaine = models.ForeignKey(Domaine, on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return self.titre

# Gimpy - Description 
Gimpy est un logiciel de traitement d'image écrit en python 3.X, utilisant la Programmation Orentientée Objet (POO). 
 
Modules utilisés : 
 - tkinter pour l'interface graphique
 - Pillow alias PIL pour le traitement d'image
 - matplotlib pour l'affichage des graphiques

Fonctions du script :
 - Ouvrir, fermer, enregistrer une image
 - Appliquer des filtres à une image (Noir et blanc, Nuances de gris, Sepia, Négatif, Flou, Symétries verticale/horizontale, Miroirs vertical/horizontal) par technique de seuillage ou matrice de convolution
 - Augmenter ou diminuer le contraste, la luminosité, la saturation d'une image
 - Afficher l'histogramme global / les histogrammes de couleur
 - Utiliser un pinceau et pouvoir choisir la couleur du pinceau grâce à une palette
 - Utiliser un algorithme de décomposition d'image (qui fractionne l'image en 4)
 - Pouvoir revenir à l'image de départ à tout moment
 
# Gimpy - Installation

Pour l'installation il faut juste télécharger le .zip via github, il comprend le script et le dossier contenant les images utiles à l'affichage de l'interface graphique.
Il faut également une version python 3.x avec les bons modules. Ils sont en général compris dans le téléchargement de python.

Pour installer les modules utilisés via cmd sous windows (Penser à mettre python dans le PATH) 

 #python -m pip install matplotlib
 
 #python -m pip install tkinter
 
 #python -m pip install Pillow

# Gimpy - Améliorations

Fonctions et idées à implémenter quand j'aurais le temps
 - Rédiger l'aide (utiliser widget Text)
 - Fenêtre paramètres pour modifier le rayon du pinceau
 - Appliquer un filtre localement avec le pinceau
 - Système de selection rectangulaire de pixels
 - Système d'historique des modifications pour ne pas avoir à tout recommencer
 

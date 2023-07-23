# Importer la librairie pygame
import pygame
# Importer seulement la fonction exit() du module sys
from sys import exit
from random import randint

class Joueur(pygame.sprite.Sprite):
    """Classe définissant le comportement général du joueur"""
    def __init__(self):
        # Fais des connexions entre les classes
        super.__init__()
        # Création des attributs de la condition initiale du joueur (image sur écr, rectangle, mode de collision)
        self.joueur_surface = pygame.image.load('Sprite/Joueur/joueur.png').convert_alpha()
        self.joueur_rect = joueur_surface.get_rect(midbottom=(440, 650))
        # Attribut du masque permettant les collisions
        self.mask = pygame.mask.from_surface(self.joueur_surface)

    def joueur_controles(self):
        # Contrôles du joueur
        controles = pygame.key.get_pressed()
        # Conditions de déplacement du joueur
        if controles[pygame.K_LEFT] and self.joueur_rect.left >= 0:
            self.joueur_rect.x -= 1
        if controles[pygame.K_RIGHT] and self.joueur_rect.right <= hauteur:
            self.joueur_rect.x += 1

    def update(self):
        self.joueur_controles()

class Obstacles(pygame.sprite.Sprite):
    """Classe définissant le comportement général des obstacles"""
    def __init__(self,type):
        super().__init__()

        # Si les obstacles sont de types différents, les afficher selon des critères différents
        if type == "charette":
            charette = pygame.image.load('Sprite/Obstacles/ImageRedi/charette.png').convert_alpha()
        if type == "pierre_arrondie":
            pierre_arrondie = pygame.image.load('Sprite/Obstacles/ImageRedi/pierre_arrondie.png').convert_alpha()
        if type == "pierre_feuille":
            pierre_feuille = pygame.image.load('Sprite/Obstacles/ImageRedi/pierre_feuille.png').convert_alpha()
        if type == "pierre_liane":
            pierre_liane = pygame.image.load('Sprite/Obstacles/ImageRedi/pierre_liane.png').convert_alpha()
        if type == "deux_pierres":
            deux_pierres = pygame.image.load('Sprite/Obstacles/ImageRedi/deux_pierres.png').convert_alpha()
        if type == "bison":
            bison = pygame.image.load('Sprite/Obstacles/ImageRedi/bison.png').convert_alpha()


def display_score():
    score_surf = score_font.render(f'{compteur}', False, (64, 64, 64))
    score_rect = score_surf.get_rect(center = (240, 20))
    fenetre.blit(score_surf, score_rect)

def pattern_1():
    """Formation en triangle"""
    # Si la pierre atteint le haut de l'écran, revenir au début et incrémenter 1 au compteur
    PierreArrondie1_rect.top -= 1
    PierreArrondie2_rect.top -= 1
    PierreArrondie3_rect.top -= 1

    if PierreArrondie1_rect.top < 0:
        PierreArrondie1_rect.x = 20
        PierreArrondie1_rect.y = 550

    if PierreArrondie2_rect.top < 0:
        PierreArrondie2_rect.x = 170
        PierreArrondie2_rect.y = 550

    if PierreArrondie3_rect.top < 0:
        PierreArrondie3_rect.x = 330
        PierreArrondie3_rect.y = 550

def pattern_3():
    """Formation en triangle inversée"""
    if PierreArrondie1_rect.top < 0:
        PierreArrondie1_rect.x = 50
        PierreArrondie1_rect.y = 450
    if PierreArrondie2_rect.top < 0:
        PierreArrondie2_rect.x = 250
        PierreArrondie2_rect.y = 550
    if PierreArrondie3_rect.top < 0:
        PierreArrondie3_rect.x = 350
        PierreArrondie3_rect.y = 450

def pattern_3():
    """L'obstacle le plus à gauche a un carré d'avance sur le reste"""
    if PierreArrondie1_rect.top < 0:
        PierreArrondie1_rect.x = 50
        PierreArrondie1_rect.y = 450
    if PierreArrondie2_rect.top < 0:
        PierreArrondie2_rect.x = 250
        PierreArrondie2_rect.y = 550
    if PierreArrondie3_rect.top < 0:
        PierreArrondie3_rect.x = 350
        PierreArrondie3_rect.y = 550

# Initialisation de la fenêtre pygame
pygame.init()
# Statut du jeu
JeuActif = True
# Initialisation des variables largeur et hauteur
largeur = 480
hauteur = 600

#Couleur du gazon en RGB
ColorGazon = "#B1F076"
# Initialisation de la fenêtre avec les largeurs et hauteurs
fenetre = pygame.display.set_mode((largeur, hauteur))
# Titrage de la fenêtre
pygame.display.set_caption('Vendange')
# Objet clock
clock = pygame.time.Clock()
# Créer une surface pleine
gazon = pygame.Surface((largeur, hauteur))
# Mettre de la couleur
gazon.fill(ColorGazon)

# .convert_alpha() : rend plus rapide Python avec les sprites des diff-t éléments
joueur_surface = pygame.image.load('Sprite/Joueur/joueur.png').convert_alpha()
joueur_position_x = 200
joueur_position_y = 100
joueur_rect = joueur_surface.get_rect(midbottom = (joueur_position_x, joueur_position_y))

PierreArrondie1_surface = pygame.image.load('Sprite/Obstacles/ImageRedi/pierre_arrondie.png').convert_alpha()
PierreArrondie1_position_x = 80
PierreArrondie1_position_y = 550
PierreArrondie1_rect = PierreArrondie1_surface.get_rect(midbottom=(PierreArrondie1_position_x,PierreArrondie1_position_y))

PierreArrondie2_surface = pygame.image.load('Sprite/Obstacles/ImageRedi/pierre_arrondie.png').convert_alpha()
PierreArrondie2_position_x = 250
PierreArrondie2_position_y = 400
PierreArrondie2_rect = PierreArrondie2_surface.get_rect(midbottom=(PierreArrondie2_position_x,PierreArrondie2_position_y))

PierreArrondie3_surface = pygame.image.load('Sprite/Obstacles/ImageRedi/pierre_arrondie.png').convert_alpha()
PierreArrondie3_position_x = 420
PierreArrondie3_position_y = 550
PierreArrondie3_rect = PierreArrondie3_surface.get_rect(midbottom=(PierreArrondie3_position_x,PierreArrondie3_position_y))

# Affichage du score
score_font = pygame.font.Font(None, 30)
score_surf = score_font.render('Score', False, '#000000')
score_rect = score_surf.get_rect(center = (240, 20))
compteur = 0

while True:
    # Pour tous les évènements présents dans la librairie pygame
    for evenement in pygame.event.get():
        # Si le type d'évènement est QUIT, fermer la fenêtre
        if evenement.type == pygame.QUIT:
            # Désinitialise pygame en laissant tourner la boucle while
            pygame.quit()
            # Permet d'arrêter pygame en arrêtant la boucle.
            exit()
        if JeuActif:
            ####
        else:
            if evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_SPACE:
                    JeuActif = True

 # Jeu actif
    if JeuActif:
        # Mettre une surface sur une autre
        fenetre.blit(gazon, (0, 0))

        # Création des cases :
        pygame.draw.aaline(fenetre, 'Black', (160, 0), (160, hauteur))
        pygame.draw.aaline(fenetre, 'Black', (320, 0), (320, hauteur))
        pygame.draw.aaline(fenetre, 'Black', (0, 150), (largeur, 150))
        pygame.draw.aaline(fenetre, 'Black', (0, 300), (largeur, 300))
        pygame.draw.aaline(fenetre, 'Black', (0, 450), (largeur, 450))
        display_score()
        fenetre.blit(joueur_surface, joueur_rect)

        ## Contrôle des boutons
        # Si on appuie sur la touche gauche du clavier et que le coin gauche du joueur ne dépasse pas l'écran à gauche,
        # le joueur se déplace à gauche. Même logique pour la touche droite.
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and (joueur_rect.left >= 0):
            joueur_rect.left -= 2
        if keys[pygame.K_RIGHT] and (joueur_rect.right <= largeur):
            joueur_rect.left += 2

        pattern_1()



# S'il y a collision entre le joueur et les obstacles, arrêter de mettre à jour le jeu et remettre à 0 le compteur
        if joueur_rect.colliderect(PierreArrondie1_rect) or joueur_rect.colliderect(PierreArrondie2_rect)\
                or joueur_rect.colliderect(PierreArrondie3_rect):
                JeuActif = False

        # Affiche la pierre arrondie
        fenetre.blit(PierreArrondie1_surface, PierreArrondie1_rect)
        fenetre.blit(PierreArrondie2_surface, PierreArrondie2_rect)
        fenetre.blit(PierreArrondie3_surface, PierreArrondie3_rect)
        # Affiche tous nos éléments (perso, raisins et charette)
        # Met à jour tout ce qu'il y aura sur la fenêtre
        pygame.display.update()
        # Taux de rafraichissement à 60Hz
        clock.tick(60)

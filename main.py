# Importer la librairie pygame
import pygame
# Importer seulement la fonction exit() du module sys
from sys import exit
from random import randint, choice

class Joueur(pygame.sprite.Sprite):
    """Classe définissant le comportement général du joueur"""
    def __init__(self):
        # Fais des connexions entre les classes
        super().__init__()
        # Création des attributs de la condition initiale du joueur (image sur écran, rect, mode de collision)
        self.image = pygame.image.load('Sprite/Joueur/joueur.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom = (120, 600))
        self.mask = pygame.mask.from_surface(self.image)

    def joueur_controles(self):
        # Controles du joueur
        controles = pygame.key.get_pressed()
        # Conditions de déplacement du joueur
        if controles[pygame.K_LEFT] and self.rect.left >= 0:
            self.rect.x -= 1
        if controles[pygame.K_RIGHT] and self.rect.right <= largeur:
            self.rect.x += 1

    def reset_position(self):
        """Réinitialise les positions x et y des obstacles"""
        self.rect.x = 120
        self.rect.y = 500

    def update(self):
        self.joueur_controles()

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()

        # Si les obstacles sont de types différents, les afficher selon des critères différents
        if type == "charette":
            charette = pygame.image.load('Sprite/Obstacles/ImageRedi/charette.png')
            position_x = randint(40, 450)
            position_y = 0
            vitesse = 3
            self.ennemi = charette
        if type == "pierre_arrondie":
            pierre_arrondie = pygame.image.load('Sprite/Obstacles/ImageRedi/pierre_arrondie.png')
            position_x1 = randint(0,70)
            position_x2 = randint(400, 460)
            position_x = randint(position_x1, position_x2)
            position_y = randint(0, 50)
            vitesse = 1
            self.ennemi = pierre_arrondie

        if type == "petit_caillou":
            petit_caillou = pygame.image.load('Sprite/Obstacles/ImageRedi/petit_caillou.png')
            position_x1 = randint(0, 70)
            position_x2 = randint(400, 460)
            position_x = randint(position_x1, position_x2)
            position_y = randint(0, 50)
            vitesse = 1
            self.ennemi = petit_caillou

        self.image = self.ennemi
        # Attribut du rectangle des rectangles
        self.rect = self.image.get_rect(midbottom = (position_x, position_y))
        # Attribut de la vitesse de déplacement des ennemis
        self.vitesse_ennemis = vitesse
        # Attribut du masque permettant les collisions de pixel à pixel
        self.mask = pygame.mask.from_surface(self.image)

    def ennemis_deplacements(self):
        """Définit les déplacements des ennemis"""
        self.rect.y += self.vitesse_ennemis
        # Si le rectangle atteint l'extérieur de l'écran, rembobiner:
        if self.rect.y < -140:
            self.kill()

    def update(self):
        self.ennemis_deplacements()


def afficher_pause():
    pause_police = pygame.font.Font('Sprite/Score/QuinqueFive.ttf', 15)
    pause_surface = pause_police.render('Pause', False, 'Black')
    fenetre.blit(pause_surface, (240, 50))


def afficher_score(score_actuel):
    score_font = pygame.font.Font('Sprite/Score/QuinqueFive.ttf', 15)
    score_surf = score_font.render(f'Score : {score_actuel}', False, 'Black')
    fenetre.blit(score_surf, (240, 20))


def collisions_obstacles_sprites():
    """Fonction pour détecter les collisions entre obstacles"""
    if pygame.sprite.spritecollide(joueur_groupe_sprite.sprite, obstacles_ennemis_groupe_sprite,False,
                                   pygame.sprite.collide_mask):
        # Arrêter le jeu
        return False
    else : return True

def game_over():
    """Fonction pour afficher l'écran de game over en cas de collision"""
    # Affectation de la police de game over (taille et type de police)
    perdu_police = pygame.font.Font('Sprite/Score/QuinqueFive.ttf', 15)
    # Affectation de la surface
    perdu_surface = perdu_police.render('Game Over', False, 'Black')
    commande_surface = perdu_police. render('Press P', False, 'Black')

    # Si collision, afficher Game over
    controle = pygame.key.get_pressed()
    if pygame.sprite.spritecollide(joueur_groupe_sprite.sprite, obstacles_ennemis_groupe_sprite, False,
                                   pygame.sprite.collide_mask):
        fenetre.blit(perdu_surface, (240, 50))
        fenetre.blit(commande_surface, (240, 80))
        joueur_groupe_sprite.sprite.reset_position()
        obstacles_ennemis_groupe_sprite.empty()


# A écrire en premier et tourner avant tout autre fonction
pygame.init()
# Variable JeuActif
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
# Créer une surface pleine
gazon = pygame.Surface((largeur, hauteur))

# Création du GroupeSingle
joueur_groupe_sprite = pygame.sprite.GroupSingle()
joueur_sprite = Joueur()
joueur_groupe_sprite.add(joueur_sprite)

obstacles_ennemis_groupe_sprite = pygame.sprite.Group()

score_actuel = 0
# Objet clock
clock = pygame.time.Clock()
# Affectation d'un evenement utilisateur customisable qui s'enclenche en certains intervalles à la variable CompteurObstacle
CompteurObstacle = pygame.USEREVENT + 1
# Appel de la fonction pygame.time.set_timer() qui s'enclenche toutes les 4 secondes
pygame.time.set_timer(CompteurObstacle, 4000)



# Mettre de la couleur
gazon.fill(ColorGazon)
# Démarrage du jeu
while True:
    # Pour tous les évènements présents dans la librairie pygame
    for evenement in pygame.event.get():
        # Si le type d'évènement est QUIT, fermer la fenêtre
        if evenement.type == pygame.QUIT:
            # Désinitialise pygame en laissant tourner la boucle while
            pygame.quit()
            # Permet d'arrêter pygame en arrêtant la boucle.
            exit()
        if evenement.type == pygame.MOUSEMOTION:
            print(evenement.pos)
        if evenement.type == CompteurObstacle and JeuActif:
            obstacles_ennemis_groupe_sprite.add(Obstacle(choice(['pierre_arrondie','pierre_arrondie','petit_caillou'
                                                                    ,'charette'])))
        if JeuActif:
            if evenement.type == pygame.KEYDOWN:
               if evenement.key == pygame.K_p:
                   afficher_pause()
                   JeuActif = False
        else:
            if evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_p:
                    JeuActif = True

    if JeuActif:
        # Jeu actif
        # Mettre une surface sur une autre
        fenetre.blit(gazon, (0, 0))
        # fenetre.blit(score_surf, score_rect)

        # Créer une forme autour du score
        # pygame.draw.rect(fenetre, 'Pink', score_rect, 1)
        # Création des cases :
        pygame.draw.aaline(fenetre, 'Black', (160, 0), (160, hauteur))
        pygame.draw.aaline(fenetre, 'Black', (320, 0), (320, hauteur))
        pygame.draw.aaline(fenetre, 'Black', (0, 150), (largeur, 150))
        pygame.draw.aaline(fenetre, 'Black', (0, 300), (largeur, 300))
        pygame.draw.aaline(fenetre, 'Black', (0, 450), (largeur, 450))

        joueur_groupe_sprite.draw(fenetre)
        joueur_groupe_sprite.update()

        obstacles_ennemis_groupe_sprite.draw(fenetre)
        obstacles_ennemis_groupe_sprite.update()

        # Collision
        JeuActif = collisions_obstacles_sprites()
        game_over()

        # Score
        score_actuel = score_actuel + 1
        afficher_score(score_actuel)
        # CompteurScore = display_score(joueur_rect, ObstaclesList, score_actuel)
    else:
        score_actuel = 0
    # Affiche tous nos éléments (perso, raisins et charette)
    # Met à jour tout ce qu'il y aura sur la fenêtre
    pygame.display.update()
    # Taux de rafraichissement à 60Hz
    clock.tick(60)
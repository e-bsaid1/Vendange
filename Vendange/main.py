# Importer la librairie pygame
import pygame
# Importer seulement la fonction exit() du module sys
from sys import exit
from random import randint

def display_score(joueur, obstacles,score_actuel):
    score_font = pygame.font.Font(None, 30)
    score_actuel = 0
    score_surf = score_font.render(f'{score_actuel}', False, (64, 64, 64))
    score_rect = score_surf.get_rect(center=(240, 20))

    if obstacles:
        fenetre.fill((255, 255, 255), rect=score_rect)
        fenetre.blit(score_surf, score_rect)
        for obstacle_rect in obstacles:
            if not joueur.colliderect(obstacle_rect) and obstacle_rect.y < 30:
                score_actuel = score_actuel + 1
    if not obstacles:
        fenetre.fill((255, 255, 255), rect=score_rect)
        fenetre.blit(score_surf, score_rect)
    pygame.display.update(score_rect)


def obstacle_mouvement(ObstaclesList):
    """Fonction gérant les mouvements et l'affichage des obstacles"""
    if ObstaclesList:
        for ObstacleRect in ObstaclesList:
            ObstacleRect.y -= 2
            if ObstacleRect.y < 300 :
                ObstacleRect.y -= 1
                fenetre.blit(Bison_surface, ObstacleRect)
            else:
                fenetre.blit(charrette_surface, ObstacleRect)

        # Si l'obstacle va beaucoup trop en haut, arrêter le mouvement
        ObstaclesList = [obstacle for obstacle in ObstaclesList if obstacle.y > 30]

        return ObstaclesList
    else :
        return []

def collisions_obstacle(joueur,obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if joueur.colliderect(obstacle_rect):
                return False
    return True


# A écrire en premier et tourner avant tout autre fonction
pygame.init()
# Variable JeuActif
JeuActif = True
# Initialisation des variables largeur et hauteur
largeur = 480
hauteur = 600
#Couleur du gazon en RGB
ColorGazon = "#B1F076"
# Compteur pour score
CompteurScore = 0
# Initialisation de la fenêtre avec les largeurs et hauteurs
fenetre = pygame.display.set_mode((largeur, hauteur))
# Titrage de la fenêtre
pygame.display.set_caption('Vendange')
# Objet clock
clock = pygame.time.Clock()
# Créer une surface pleine
gazon = pygame.Surface((largeur, hauteur))
# .convert_alpha() : rend plus rapide Python avec les sprites des diff-t éléments
joueur_surface = pygame.image.load('Sprite/Joueur/joueur.png').convert_alpha()
joueur_position_x = 200
joueur_position_y = 100
joueur_rect = joueur_surface.get_rect(midbottom = (joueur_position_x, joueur_position_y))

# Affichage du score
# score_surf = score_font.render('Score', False, '#000000')
# score_rect = score_surf.get_rect(center = (240, 20))
# Nombre pour passer d'une frame à un autre
nombre = 0
# Création du rectangle charrette dans l'écran
charrette_surface = pygame.image.load('Sprite/Obstacles/ImageRedi/charette.png').convert_alpha()
# Position initiale x-y de la charrette
charrette_position_x = 250
charrette_position_y = 550
charrette_position_x2 = 420
charrette_position_y2 = randint(300, 550)
charrette_position_x3 = 85
charrette_position_y3 = randint(300, 500)

charrette_rect = charrette_surface.get_rect(midbottom = (charrette_position_x, charrette_position_y))

# Création du rectangle pierre dans l'écran

PierreArrondie_surface = pygame.image.load('Sprite/Obstacles/ImageRedi/pierre_arrondie.png').convert_alpha()
PierreArrondie_position_x = 80
PierreArrondie_position_y = 550
PierreArrondie_rect = PierreArrondie_surface.get_rect(midbottom=(PierreArrondie_position_x, PierreArrondie_position_y))

# Création de l'obstacle chien dans l'écran
Bison_surface = pygame.image.load('Sprite/Obstacles/ImageRedi/bison.png').convert_alpha()
Bison_position_x = 20
Bison_position_y = 300
Bison_rect = Bison_surface.get_rect(midbottom=(Bison_position_x, Bison_position_y))

ObstaclesList = []
# Chronomètre
CompteurObstacle = pygame.USEREVENT + 1
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
        if JeuActif:
            if evenement.type == pygame.MOUSEMOTION:
                print(evenement.pos)
        else:
            if evenement.type == pygame.KEYDOWN:
                JeuActif = False
                if evenement.key == pygame.K_SPACE:
                    charrette_rect.bottom = 500
                    JeuActif = True

        if evenement.type == CompteurObstacle and JeuActif:
            nombre = randint(1, 5)
            if nombre == 1:
                ObstaclesList.append(charrette_surface.get_rect(midbottom=(charrette_position_x, charrette_position_y)))
                ObstaclesList.append(charrette_surface.get_rect(midbottom=(charrette_position_x2, charrette_position_y2)))
                ObstaclesList.append(charrette_surface.get_rect(midbottom=(charrette_position_x3, charrette_position_y3)))
            if nombre == 2:
                ObstaclesList.append(charrette_surface.get_rect(midbottom=(80, 400)))
                ObstaclesList.append(charrette_surface.get_rect(midbottom=(250, 550)))
                ObstaclesList.append(charrette_surface.get_rect(midbottom=(420, 550)))
            if nombre == 3:
                ObstaclesList.append(charrette_surface.get_rect(midbottom=(80, 400)))
                ObstaclesList.append(charrette_surface.get_rect(midbottom=(250, 550)))
                ObstaclesList.append(charrette_surface.get_rect(midbottom=(420, 400)))
            if nombre == 4:
                ObstaclesList.append(charrette_surface.get_rect(midbottom=(80, 550)))
                ObstaclesList.append(charrette_surface.get_rect(midbottom=(250, 550)))
                ObstaclesList.append(charrette_surface.get_rect(midbottom=(420, 400)))
            else:
                ObstaclesList.append(Bison_surface.get_rect(topleft=(Bison_position_x, Bison_position_y)))
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
     fenetre.blit(joueur_surface, joueur_rect)

     # Mouvement de l'obstacle
     ObstaclesList = obstacle_mouvement(ObstaclesList)

     # Collision
     JeuActif = collisions_obstacle(joueur_rect, ObstaclesList)

     # Score
     CompteurScore = display_score(joueur_rect, ObstaclesList, CompteurScore)

     ## Contrôle des boutons
     # Si on appuie sur la touche gauche du clavier et que le coin gauche du joueur ne dépasse pas l'écran à gauche,
     # le joueur se déplace à gauche. Même logique pour la touche droite.
     keys = pygame.key.get_pressed()
     if keys[pygame.K_LEFT] and (joueur_rect.left >= 0):
         joueur_rect.left -= 3
     if keys[pygame.K_RIGHT] and (joueur_rect.right <= largeur):
         joueur_rect.left += 3

    # Si la charrette atteint le haut de l'écran, revenir au début et incrémenter 1 au compteur

    # S'il y a collision entre le joueur et les obstacles, arrêter de mettre à jour le jeu et remettre à 0 le compteur
    # if joueur_rect.colliderect(PierreArrondie_rect) or joueur_rect.colliderect(charrette_rect):
# JeuActif = False


    # Affiche tous nos éléments (perso, raisins et charette)
    # Met à jour tout ce qu'il y aura sur la fenêtre
    pygame.display.update()
    # Taux de rafraichissement à 60Hz
    clock.tick(60)
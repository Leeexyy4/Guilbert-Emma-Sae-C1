
from enum import Enum
import pygame
from interface import Interface
from utils import image, texte

class Client_State(Enum):

    
    LOCAL = 2 # création de la map, envoi des donné au joueur

    ONLINE = 3 # attente que le MAX_PLAYER sois atteint
    MENU = 1 # creation d'une instance de serveur
    
    STARTING = 2 # création de la map, envoi des donné au joueur

    WAIT_CONNECION = 3 # attente que le MAX_PLAYER sois atteint
    
    IN_GAME = 4 # boucle de jeu principal

    QUIT = 5 # fin du serveur envoi des donné à la bd pour les stat
    


class Menu_State(Enum):

    INDEX = 1 # creation d'une instance de serveur    
    GLOBALS_STATS = 4 # boucle de jeu principal
    HELPER = 5 # fin du serveur envoi des donné à la bd pour les stat
    NB_PLAYER = 6
    NB_IA = 7

class Main():
    def __init__(self) -> None:
        self.__clock:pygame.time.Clock =  pygame.time.Clock()
        self.__screen = pygame.display.set_mode((800, 700))
        self.__stateMenu:Menu_State = None
        self.__stateClient:Client_State = None
        self.__interface:Interface = None
        self.main()
        
    def go_to_menu(self, menu_state:Menu_State):
        self.__stateMenu = menu_state
        print(self.__stateMenu)
        self.change_state(Client_State.MENU)
    def change_state(self, client_state:Client_State):
        self.__stateClient = client_state
        if self.__stateClient == Client_State.MENU: self.__interface = None
        print(self.__stateClient)

    def draw(self):
        
        match self.__stateClient :
            case Client_State.MENU:
                print(self.__stateMenu)
                match self.__stateMenu :
                    case Menu_State.INDEX:
                        # Affiche l'image de fond 
                        image.Image(0,0,image.Page.DEBUT_JEU.value).affichage_image_redimensionnee(800, 700,self.__screen)
                    case Menu_State.GLOBALS_STATS:
                        image.Image(0,0,image.Page.STATS.value).affichage_image_redimensionnee(800, 700,self.__screen)
                    case Menu_State.HELPER:
                        image.Image(0, 0, image.Page.COMMANDES.value).affichage_image_redimensionnee(800, 700,self.__screen)
                    case Menu_State.NB_IA:
                        selectable_nb_ia = self.__interface.selectable_nb_ia()
                        image.Image(0, 0, image.Page.CHOIX_NB_IA.value).affichage_image_redimensionnee(800, 700,self.__screen)
                        if 1 in selectable_nb_ia :
                            image.Image(400, 595, image.BtnMenu.BTN_0.value).affiche(self.__screen)
                            image.Image(500, 595, image.BtnMenu.BTN_1.value).affiche(self.__screen)
                            image.Image(600, 595, image.BtnMenu.BTN_2.value).affiche(self.__screen)
                            image.Image(700, 595, image.BtnMenu.BTN_3.value).affiche(self.__screen)
                        if 2 in selectable_nb_ia :
                            image.Image(400, 595, image.BtnMenu.BTN_0.value).affiche(self.__screen)
                            image.Image(500, 595, image.BtnMenu.BTN_1.value).affiche(self.__screen)
                            image.Image(600, 595, image.BtnMenu.BTN_2.value).affiche(self.__screen)
                        if 3 in selectable_nb_ia :
                            image.Image(400, 595, image.BtnMenu.BTN_0.value).affiche(self.__screen)
                            image.Image(500, 595, image.BtnMenu.BTN_1.value).affiche(self.__screen)
                        if 4 in selectable_nb_ia :
                            texte.Texte("Le nombre de joueurs est complet tu ne peux pas ajouter d'IA", self.get_couleur().get_Noir(), 30, 600).affiche(self.get_police(),self.__screen)


                    case Menu_State.NB_PLAYER:
                        image.Image(0, 0, image.Page.CHOIX_NB_JOUEUR.value).affichage_image_redimensionnee(800, 700,self.__screen)
                        image.Image(400, 595, image.BtnMenu.BTN_1.value).affiche(self.__screen)
                        image.Image(500, 595, image.BtnMenu.BTN_2.value).affiche(self.__screen)
                        image.Image(600, 595, image.BtnMenu.BTN_3.value).affiche(self.__screen)
                        image.Image(700, 595, image.BtnMenu.BTN_4.value).affiche(self.__screen)
        self.__clock.tick(60)
        pygame.display.update()
            
    def mouse_on_btn_back(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        return (10 <= mouse_x <= 70 and 630 <= mouse_y <= 690)

    def menu_logical(self,mouse_x:int, mouse_y:int, is_cliked:bool):
        match self.__stateMenu :
            case Menu_State.INDEX:
                if is_cliked:
                    if (320 <= mouse_x <= 470 and 500 <= mouse_y <= 550) : # si appuie bouton stats
                        self.go_to_menu(Menu_State.GLOBALS_STATS)
                    if (170 <= mouse_x <= 350 and 550 <= mouse_y <= 600) : # si appuie bouton en local
                        self.go_to_menu(Menu_State.NB_PLAYER)
                        self.__interface = Interface(False)
                    if (450 <= mouse_x <= 630 and 550 <= mouse_y <= 600) : # si appuie bouton en ligne
                        self.go_to_menu(Menu_State.NB_PLAYER)
                        self.__interface = Interface(True)
                        
                    if 700 <= mouse_x <= 764 and 25 <= mouse_y <= 89 : # si appuie sur info
                        self.go_to_menu(Menu_State.HELPER)
                    if (Main.mouse_on_btn_back()): # si appuie sur fleche retour
                        self.go_to_menu(Menu_State.INDEX)
                pass
            case Menu_State.GLOBALS_STATS:
                if is_cliked:
                    if (40 <= mouse_x <= 100 and 40 <= mouse_y <= 100): # si appuie sur fleche retour
                        self.go_to_menu(Menu_State.INDEX)
                        stats = True
                pass
            case Menu_State.HELPER:
                if is_cliked:
                    if (Main.mouse_on_btn_back()): # si appuie sur fleche retour
                        self.go_to_menu(Menu_State.INDEX)
                pass
            
            case Menu_State.NB_IA:
                # Recuperer les coordonnees de la souris
                selectable_nb_ia = self.__interface.selectable_nb_ia()
                if is_cliked:
                    if (40 <= mouse_x <= 100 and 40 <= mouse_y <= 100) : # si appuie bouton play
                        self.__interface.set_nb_IA(0)
                        self.go_to_menu(Menu_State.NB_PLAYER)
                    
                    # Si le personnage sur lequel on clique est J1
                    if 400 <= mouse_x <= 500 and 582 <= mouse_y <= 652 and 0 in selectable_nb_ia:   
                        self.__interface.set_nb_IA(0)
                        self.change_state(Client_State.ONLINE if self.__interface.is_online()  else Client_State.LOCAL)
                    # Si le personnage sur lequel on clique est J2   
                    if 500 <= mouse_x <= 600 and 582 <= mouse_y <= 652 and 1 in selectable_nb_ia:
                        self.__interface.set_nb_IA(1)
                        self.change_state(Client_State.ONLINE if self.__interface.is_online() else Client_State.LOCAL)
                    # Si le personnage sur lequel on clique est J3
                    if 600 <= mouse_x <= 700 and 582 <= mouse_y <= 652 and 2 in selectable_nb_ia:   
                        self.__interface.set_nb_IA(2)
                        self.change_state(Client_State.ONLINE if self.__interface.is_online() else Client_State.LOCAL)
                    # Si le personnage sur lequel on clique est J4
                    if 700 <= mouse_x <= 800 and 582 <= mouse_y <= 652 and 3 in selectable_nb_ia:   
                        self.__interface.set_nb_IA(3)
                        self.change_state(Client_State.ONLINE if self.__interface.is_online() else Client_State.LOCAL)
                pass
            case Menu_State.NB_PLAYER:
                if is_cliked:
                    if (40 <= mouse_x <= 100 and 40 <= mouse_y <= 100) : # si appuie bouton play
                        self.__interface = None
                        self.go_to_menu(Menu_State.INDEX)
                    # Si le personnage sur lequel on clique est J2   
                    if 500 <= mouse_x <= 600 and 582 <= mouse_y <= 652 :
                        self.__interface.set_nb_joueur(2)
                        if self.__interface.is_online():
                            self.change_state(Client_State.STARTING)
                        else:
                            self.go_to_menu(Menu_State.NB_IA)
                    # Si le personnage sur lequel on clique est J4
                    if 700 <= mouse_x <= 800 and 582 <= mouse_y <= 652 :   
                        self.__interface.set_nb_joueur(4)
                        if self.__interface.is_online():
                            self.change_state(Client_State.STARTING)
                        else:
                            self.go_to_menu(Menu_State.NB_IA)
                    # Si le personnage sur lequel on clique est J1
                    if 400 <= mouse_x <= 500 and 582 <= mouse_y <= 652 :   
                        self.__interface.set_nb_joueur(1)
                        if self.__interface.is_online():
                            self.change_state(Client_State.STARTING)
                        else:
                            self.go_to_menu(Menu_State.NB_IA)
                    # Si le personnage sur lequel on clique est J3
                    if 600 <= mouse_x <= 700 and 582 <= mouse_y <= 652 :   
                        self.__interface.set_nb_joueur(3)
                        if self.__interface.is_online():
                            self.change_state(Client_State.STARTING)
                        else:
                            self.go_to_menu(Menu_State.NB_IA)
                    pass
    
    def game_logical(self,mouse_x:int, mouse_y:int, is_cliked:bool):
        if self.__interface == None:
            self.go_to_menu(Menu_State.INDEX)
            return
    def main(self):
        self.go_to_menu(Menu_State.INDEX)
        while (self.__stateClient != Client_State.QUIT):
            click = False
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # si le joueur quitte la fenetre # si le joueur quitte la fenetre
                    pygame.quit()
                    self.__stateClient = Client_State.QUIT
                    
                if(event.type == pygame.MOUSEBUTTONUP): click = True
                # print(click)
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_z:
                        pass
                    
                    
                    
            mouse_x, mouse_y = pygame.mouse.get_pos()
            match self.__stateClient :
                case Client_State.MENU:
                    self.menu_logical(mouse_x, mouse_y, click)
                case Client_State.LOCAL:
                    pass
                case Client_State.ONLINE:
                    pass
                case Client_State.QUIT:
                    pass
            self.draw()
            
            
            
            
            
Main()
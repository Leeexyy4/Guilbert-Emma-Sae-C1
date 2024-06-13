# ----------------------- Jeu de plateau - Rectangle  ------------------------ #

# Bibliotheques utilisees pour le code
import pygame 

pygame.init()

class Rectangle:
    """La classe Rectangle est une classe qui permet de creer les rectangles du menu"""
    
    # Initialisation du plateau        
    def __init__(self,x,y,largeur,hauteur) -> None:
        """_summary_
            Initialisation du Rectangle
        """
        self.__x = x
        self.__y = y
        self.__largeur = largeur
        self.__hauteur = hauteur
    
    # Definition des getters
    def get_x(self):
        """_summary_
            Getter de la position x
        """
        return self.__x
    
    def get_y(self):
        """_summary_
            Getter de la position y
        """
        return self.__y
    
    def get_largeur(self):
        """_summary_
            Getter de la largeur du rectangle
        """
        return self.__largeur
    
    def get_hauteur(self):
        """_summary_
            Getter de la hauteur du rectangle
        """
        return self.__hauteur
    
    def get_couleur(self):
        """_summary_
            Getter de la couleur du rectangle
        """
        return self.__couleur
    
    # Definition des setters
    def set_x(self,x):
        """_summary_
            Setter de la position x
        """
        self.__x = x
    
    def set_y(self,y):
        """_summary_
            Setter de la position y
        """
        self.__y = y
        
    def set_largeur(self,largeur):
        """_summary_
            Setter de la largeur du rectangle
        """
        self.__largeur = largeur
    
    def set_hauteur(self, hauteur):
        """_summary_
            Setter de la hauteur du rectangle
        """
        self.__hauteur = hauteur
    
    def set_couleur(self, couleur):
        """_summary_
            Setter de la couleur du rectangle
        """
        self.__couleur = couleur
    
    # Definir l'affichage du rectangle sur l'interface'
    def affiche(self,surface,couleur):
        """_summary_
            La fonction affiche affiche le rectangle et ses contours noirs sur l'interface pygame(Surface surface, Triplet int couleur)
        """
        pygame.draw.rect(surface,couleur,(self.__x,self.__y,self.__largeur,self.__hauteur))
        
        # Dessiner les bords de la place pour les cles
        pygame.draw.line(surface,(0, 0, 0),(self.__x,self.__y),(self.__x + self.__largeur,self.__y),2)
        pygame.draw.line(surface,(0, 0, 0),(self.__x,self.__y),(self.__x,self.__y + self.__hauteur),2)
        pygame.draw.line(surface,(0, 0, 0),(self.__x + self.__largeur,self.__y),(self.__x + self.__largeur,self.__y + self.__hauteur),2)
        pygame.draw.line(surface,(0, 0, 0),(self.__x ,self.__y + self.__hauteur),(self.__x + self.__largeur,self.__y + self.__hauteur),2)
        return

    def affiche_contour(self,surface,contour):
        """_summary_
            La fonction affiche affiche le rectangle et ses contours noirs sur l'interface pygame(Surface surface, Triplet int couleur)
        """        
        # Dessiner les bords de la place pour les cles
        pygame.draw.line(surface,contour,(self.__x,self.__y),(self.__x + self.__largeur,self.__y),5)
        pygame.draw.line(surface,contour,(self.__x,self.__y),(self.__x,self.__y + self.__hauteur),5)
        pygame.draw.line(surface,contour,(self.__x + self.__largeur,self.__y),(self.__x + self.__largeur,self.__y + self.__hauteur),5)
        pygame.draw.line(surface,contour,(self.__x ,self.__y + self.__hauteur),(self.__x + self.__largeur,self.__y + self.__hauteur),5)
        return
    
    def affiche_contour_couleur(self,surface,contour,couleur):
        """_summary_
            La fonction affiche affiche le rectangle et ses contours colores sur l'interface pygame(Surface surface, Triplet int couleur)
        """     
        
        pygame.draw.rect(surface,couleur,(self.__x,self.__y,self.__largeur,self.__hauteur))
           
        # Dessiner les bords de la place pour les cles
        pygame.draw.line(surface,contour,(self.__x,self.__y),(self.__x + self.__largeur,self.__y),5)
        pygame.draw.line(surface,contour,(self.__x,self.__y),(self.__x,self.__y + self.__hauteur),5)
        pygame.draw.line(surface,contour,(self.__x + self.__largeur,self.__y),(self.__x + self.__largeur,self.__y + self.__hauteur),5)
        pygame.draw.line(surface,contour,(self.__x ,self.__y + self.__hauteur),(self.__x + self.__largeur,self.__y + self.__hauteur),5)
        return
        
# Tests des fonctions
"""
if __name__ == "__main__":
    
    import couleur
    
    nouveau_rectangle = Rectangle(50,50,100,100)
    nouveau_rectangle.affiche(pygame.display.set_mode((700,800)),couleur.Couleur().get_Beige())
"""
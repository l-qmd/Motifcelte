from turtle import *

setposition(0,0)
title("Projet Motif Celte: Lorian")

#Parti motif celte : Triskelle 
def motif1(dim,couleur):
    """Cet fonction construit une première patte du triskelle"""
    fillcolor(couleur)
    begin_fill()
    right(60)
    circle(dim,180) #fait un premier demi-cercle
    circle(dim/2,180)#fait un deuxième demi-cercle plus petit
    circle(dim/4,180)#Et enfin un dernier demi cercle encore plus petit du précédent
    penup()
    circle(dim/8,-180)
    pendown()
    circle(dim/8,-180)
    penup()
    circle(dim/8,-180)
    pendown()# Remplissage
    circle(dim/4,-180)
    circle(dim*0.75,-270)
    
def motif2(dim,couleur):
    """Cet fonction construit une deuxième patte du triskelle"""
    setheading(60)
    circle(dim,180)#fait un premier demi-cercle
    circle(dim/2,180)#fait un deuxième demi-cercle plus petit
    circle(dim/4,180)#Et enfin un dernier demi cercle encore plus petit du précédent
    penup()
    circle(dim/8,-180)
    pendown()
    circle(dim/8,-180)
    penup()
    circle(dim/8,-180)
    pendown()#Remplisage
    circle(dim/4,-180)
    circle(dim*0.75,-270)
    
def motif3(dim,couleur):
    """Cette fonction contruit la dernière patte du kristelle """
    setheading(180) 
    circle(dim,180)#fait un premier demi-cercle
    circle(dim/2,180)#fait un deuxième demi-cercle plus petit
    circle(dim/4,180)#Et enfin un dernier demi cercle encore plus petit du précédent
    penup()
    circle(dim/8,-180)
    pendown()
    circle(dim/8,-180)
    penup()
    circle(dim/8,-180)
    pendown()#Remplisage
    circle(dim/4,-180)
    circle(dim*0.75,-270)   
    end_fill()
    
#Parti 2 frise : Demi-rosas
    
def rosas(dim):
    """cet fonction fait une rosas"""
    width(4)
    speed(20)
    left(90)
    circle(dim,180)
    
def demirosas(dim):
    """Cet fonction fait une demi rosas"""
    speed(20)
    right(270)
    circle(dim , 90)

def demirosasarrière(dim):
    """Cet fonction fai un demi cercle en arrière"""
    left(180)
    circle(dim, 90)
    
def traie(dim):
    """Cet fonction renvoie deux traie un en haut et un en bat"""
    speed(20)
    width(4)
    forward(dim * 2 )
    left(90)
    penup()
    forward(dim)
    pendown()
    right(90)
    backward(dim * 2)
    penup()
    right(90)
    forward(dim)
    left(90)
    pendown()
    forward(dim * 2 )
    
#Parti 3 motifNoeud : 

def rectangle(dim,couleur):
    """cette fonction construit un rectangle"""
    pendown()
    fillcolor(couleur)
    begin_fill()
    for i in range(2):
        forward(dim )
        left(90)
        forward(dim / 8 )
        left(90)
    end_fill()

def demicercle(dim,couleur):
    """cette fonction construit une demi cercle"""
    fillcolor(couleur)
    begin_fill()
    circle(9*dim/16,180)
    left(90)
    forward(dim/8)
    right(-90)
    circle(-7*dim/16,180)
    left(90)
    forward(dim/8)
    end_fill()
 
def decaleverslehaut(dim,couleur):
    """cette fonction decale les rectangles vers le haut"""
    penup()
    left(90)
    forward(dim / 4)
    right(90)
    
def decalageversladroite(dim,couleur):
    """cette fonction decale vers la droite les rectangles contruits"""
    penup()
    right(90)
    forward(dim/4)
       
def appelle(dim,couleur):
    """cette fonction appelle toutes les fonctions nécéssaire pour construire des rectangles vers le haut"""
    for k in range(4):
        rectangle(dim,couleur)
        decaleverslehaut(dim,couleur)
        
def appelle1(dim,couleur):
    """cette fonction appelle toutes les foncions nécéssaire pour contruire des rectangles vers la droite"""
    setposition(0,0)
    for k in range(5):
        left(90)
        rectangle(dim,couleur)
        decalageversladroite(dim,couleur)

def decalerectangleenhaut(dim,couleur):
    """cette fonction forme un rectangle tous en haut de la figure pour compléter le vide"""
    setposition(0,0)
    forward(-dim/8)
    left(90)
    forward(dim)
    right(90)
    rectangle(dim,couleur)
    
def carre(dim,couleur):
    """cette fonction forme une petit carre noir pour compléter le video entre le rectangle et la figure"""
    fillcolor(couleur)
    begin_fill()
    for k in range(4):
        forward(dim/8)
        left(90)
    end_fill()
    
def rectanglemanquant(dim,couleur):
    """appelle les différentes fonctions pour former le rectangle manquant"""
    decalerectangleenhaut(dim ,couleur)
    forward(dim)
    carre(dim,couleur)
    penup()
    setposition(0,0)
    
def demicercleautour(dim,couleur):
    """Cette fonction appelle la fonction demi-cercle qui va placer les demi cerlces autours de la figure"""
    forward(-dim/8)
    right(90)
    pendown()
    demicercle(dim,couleur)
    for k in range(3):
        right(90)
        forward(dim + dim/8)
        left(90)
        demicercle(dim,couleur)

def entrelacehoronzitauxbas(dim,couleur):
    """cette fonction créer des entrelacement a sur le dernier rectangle tous en bas"""
    setposition(-dim/8,0)
    pencolor("white")
    pensize(1)
    for k in range(2):
        pendown()
        setheading(0)
        forward(9*dim/8)
        forward(-9*dim/8)
        penup()
        setheading(90)
        forward(dim/8)
        
def entrelacehoronzitauxhaut(dim,couleur):
    """cette fonction créer des entrelacement a sur le dernier rectangle tous en haut"""
    setposition(-dim/8,8*dim/8)
    pencolor("white")
    pensize(1)
    for k in range(2):
        pendown()
        setheading(0)
        forward(9*dim/8)
        forward(-9*dim/8)
        penup()
        setheading(90)
        forward(dim/8)
        
def entrelacementhoronzitaux(dim,couleur):
    """ cette fonction forme les entrecelaments entre les différents rectangles"""
    setx(-dim/8)
    pencolor("white")
    pensize(1)
    penup()
    setheading(0)
    forward(dim/4)
    pendown()
    forward(dim/8)
    penup()
    forward((dim/4) + (dim/8))
    pendown()
    forward(dim/8)
    
def decalehoronzitalaux(dim,couleur):
    """cette fonction appelle la fonction entrelacementhoronzitaux et la déplace au bonne endroit"""
    sety(dim/4)
    entrelacementhoronzitaux(dim,couleur)
    penup()
    left(90)
    forward(dim/8)
    entrelacementhoronzitaux(dim,couleur)
    penup()
    sety(dim/2 + dim/4)
    entrelacementhoronzitaux(dim,couleur)
    penup()
    left(90)
    forward(dim/8)
    entrelacementhoronzitaux(dim,couleur)
    

def  entrelacementhcentrale(dim,couleur):
    """Cette fonction forme les entrelassement au milieux de la figure"""
    penup()
    setposition(-dim/8, dim/4 + dim/4)
    pencolor("white")
    pensize(1)
    forward(dim/2)
    pendown()
    forward(dim/8)
    penup()
    setheading(90)
    forward(dim/8)
    pendown()
    setheading(0)
    forward(-dim/8)
  
def entrelacementhorizontalecentre(dim,couleur):
    """cette fonction créer des entrelacement  sur les rectangles de forme de traie blanc vers l'horizontale au centre """
    penup()
    sety(dim/4 + dim/4)
    pencolor("white")
    pensize(1)
    pendown()
    setheading(90)
    forward(dim/8)
    penup()
    setheading(0)
    forward(dim/8)
    setheading(270)
    pendown()
    forward(dim/8)
    
def decalehaurizontalecentre(dim,couleur):
    """cette fonction appelle la fonction entrelacementhorizontalecentre et la décale vers la droite former la figure"""
    penup()
    setx(dim/8)
    entrelacementhorizontalecentre(dim,couleur)
    penup()
    setx(dim/2 + dim/8)
    entrelacementhorizontalecentre(dim,couleur)
    
def entrelacementverticalecentre(dim,couleur):
    """cette fonction créer des entrelacement  sur les rectangles de forme de traie blanc vers la verticale au centre """
    pencolor("white")
    pensize(1)
    penup()
    setx(dim/4+ dim/8)
    pendown()
    forward(dim/8)
    penup()
    setheading(0)
    forward(dim/8)
    setheading(270)
    pendown()
    forward(dim/8)
    
def decaleverticalecentre(dim,couleur):
    """cette fonction appelle la fonction entrelacementverticalecentre et la décale vers le haut"""
    penup()
    sety(dim/4)
    left(180)
    entrelacementverticalecentre(dim,couleur)
    penup()
    setx(dim/4+ dim/8)
    sety(dim/2 + dim/4)
    left(180)
    entrelacementverticalecentre(dim,couleur)

#Fonction exécution des différentes partie
    
def motifCelte(dim,couleur):
    """Cet fonction appelle les autres fonction nécéssaire au fonctionnement de la forme du triskelle"""
    motif1(dim,couleur)
    motif2(dim,couleur)
    motif3(dim,couleur)

def frise(dim,repetion):
    """cet fonction appelle motif qui le répète"""
    for i in range(repetion):
        traie(dim)
        rosas(dim)
        demirosas(dim)
        demirosasarrière(dim)
        
def motifNoeud(dim,couleur):
    """cette fonction appelle toutes les fonctions nécéssaires pour former le motif avec les entrelacements"""
    appelle(dim,couleur)
    appelle1(dim,couleur)
    rectanglemanquant(dim,couleur)
    demicercleautour(dim,couleur)
    entrelacehoronzitauxbas(dim,couleur)
    entrelacehoronzitauxhaut(dim,couleur)
    decalehoronzitalaux(dim,couleur)
    entrelacementhcentrale(dim,couleur)
    decalehaurizontalecentre(dim,couleur)
    decaleverticalecentre(dim,couleur)        


#Execution des différentes partis

speed(0)

# motifCelte(200,"Black",)

# frise(100,3)

motifNoeud(200,"black")

exitonclick()
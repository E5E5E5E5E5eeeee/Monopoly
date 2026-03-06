from fonction import *
from random import *
case = 0
dernier_de = 0
carte = ""
c = ""
portefeuille = 0
propriete = ""
achat = ""
prix = ""
D = [100, 400, 150, 400, 125, 350]
P01 = [125, 350, 175, 325, 166, 265]
CHANCE0 = [166, 265, 250, 300, 196, 205]
P02 = [196, 205, 250, 225, 226, 145]
PRISON = [226, 145, 250, 100, 274, 145]
P11 = [274, 145, 250, 225, 303, 205]
CHANCE1 = [303, 205, 250, 300, 332, 265]
P12 = [332, 265, 323, 325, 375, 350]
GARE = [375, 350, 350, 400, 400, 400]
PE1 = [350, 400, 323, 325, 300, 400]
CHANCE2 = [200, 400, 250, 300, 300, 400]
PE2 = [150, 400, 175, 325, 200, 400]
plateau =  [D, P01, CHANCE0, P02, PRISON, P11, CHANCE1, P12, GARE, PE1, CHANCE2, PE2]

def setup():
    size(500, 500)

def draw():
    global dernier_de, case, plateau, portefeuille, carte, c, propriete, achat, prix
    background(18, 164, 217)
    fill(150, 200, 250)
    triangle(100, 400, 400, 400, 250, 100)
    affichage(plateau, case)
    fill(255)
    textSize(25)
    text("Resultat du de:" + str(dernier_de), 20, 50)
    text("portefeuille:" + str(portefeuille) + " euros", 20, 80)
    text("Cartes chance" , 320, 85)
    fill(0)
    text(carte , 375, 160)
    text(c , 375, 190)
    text(propriete , 20, 125)
    fill(255)
    text(achat , 20, 210)
    text(prix , 20, 240)
    
def mouseClicked():
    global case, dernier_de, portefeuille, carte, c, propriete, achat, prix
    resultat = lancer_de(plateau, case)
    resultat = prison(case, resultat)
    if resultat > 0:
        case = (resultat + case) % len(plateau) 
        dernier_de = resultat
    portefeuille, case, carte, c = chance(case, plateau, portefeuille, carte, c)
    portefeuille = depart(case, portefeuille)
    propriete, prix = proprietee(case, propriete, prix, portefeuille)
    achat, portefeuille = acheter(case, portefeuille, achat, prix)

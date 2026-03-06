from random import *
def affichage(plateau, case):
    fill(226, 216, 16)
    rect(375, 100, 110, 145)
    triangle(166, 265, 250, 300, 196, 205)                            #CHANCE0
    triangle(303, 205, 250, 300, 332, 265)                            #CHANCE1
    triangle(200, 400, 250, 300, 300, 400)                            #CHANCE2
    fill(217, 19, 138)
    triangle(226, 145, 250, 100, 274, 145)                            #PRISON
    triangle(100, 400, 150, 400, 125, 350)                            #D
    triangle(375, 350, 350, 400, 400, 400)                            #GARE
    fill(50, 46, 47)
    square(20, 140, 120)
    triangle(125, 350, 175, 325, 166, 265)                            #P01
    triangle(196, 205, 250, 225, 226, 145)                            #P02
    triangle(274, 145, 250, 225, 303, 205)                            #P11
    triangle(332, 265, 323, 325, 375, 350)                            #P12
    triangle(350, 400, 323, 325, 300, 400)                            #PE1
    triangle(150, 400, 175, 325, 200, 400)                            #PE2
    fill(50, 50, 250)
    circle((plateau[case][0] + plateau[case][2] +plateau[case][4])//3,
            (plateau[case][1] + plateau[case][3] +plateau[case][5])//3, 15)
    

def lancer_de(plateau, case):
    if dist((plateau[case][0] + plateau[case][2] +plateau[case][4])//3, (plateau[case][1] + plateau[case][3] +plateau[case][5])//3,
             mouseX, mouseY)<=50 :
        de = 1
        return de
    return 0

def chance(case, plateau, argent, carte, c):
    if (case == 2 or case == 6 or case == 10) and dist(400, 170, mouseX, mouseY)<=50:
        action = randint(1, 6)
        if action == 1:
            argent += 5000
            carte = "+" + str(argent)
            c = ""
            case = (1 + case) % len(plateau)
            return argent, case, carte, c
        elif action == 2:
            argent += 7500
            carte = "+" + str(argent)
            c = ""
            case = (1 + case) % len(plateau)
            return argent, case, carte, c
        elif action == 3:
            case = 0
            carte = "case "
            c = "depart"
            return argent, case, carte, c
        elif action == 4:
            case = (10 + case) % len(plateau)
            carte = "recule de"
            c = " 2 case"
            return argent, case, carte, c
        elif action == 5:
            case = (11 + case) % len(plateau)
            argent += -2500
            carte = "+" + str(argent)
            c = ""
            return argent, case, carte, c
        elif action == 6:
            case = 4
            carte = "PRISON!" 
            c = ""
            return argent, case, carte, c
    return argent, case, carte, c

def depart(case, portefeuille):
    if case == 0:
        portefeuille += 1000
    return portefeuille
        
def prison(case, de):
    if case == 4 and de != 1:
        de = 0
        return de 
    else:
        return de
    
def proprietee(case, propriete, prix, portefeuille):
    if case == 0 and portefeuille < 4000 and portefeuille > 0:
        propriete ="Cliquer sur le pion bleu "
        prix = "no vente"
        return propriete, prix
    elif case == 0 :
        propriete ="Case depart +1000 "
        prix = "no vente"
        return propriete, prix
    elif case == 1 :
        propriete ="Rue de la Paix"
        prix = 25000
        return propriete, prix
    elif case == 2 and portefeuille < 3000:
        propriete ="Case chance cliquer sur la carte jaune"
        prix = "no vente"
        return propriete, prix
    elif case == 2 :
        propriete ="Case chance "
        prix = "no vente"
        return propriete, prix
    elif case == 3 :
        propriete ="Avenue Henri-Martin"
        prix = 16000
        return propriete, prix
    elif case == 4 :
        propriete ="Prison faire 3 pour sortir "
        prix = "no vente"
        return propriete, prix
    elif case == 5 :
        propriete ="Boulevard de La Villette"
        prix = 25000
        return propriete, prix
    elif case == 6 :
        propriete ="Case chance "
        prix = "no vente"
        return propriete, prix
    elif case == 7 :
        propriete ="Ecole Paul Bert"
        prix = 50000
        return propriete, prix
    elif case == 8 :
        propriete ="Gare"
        prix = 5550000
        return propriete, prix
    elif case == 9 :
        propriete ="Vieux port"
        prix = 45000
        return propriete, prix
    elif case == 10 :
        propriete ="Case chance "
        prix = "no vente"
        return propriete, prix
    elif case == 11 :
        propriete ="Hotel de ville"
        prix = 10000
        return propriete, prix
    return "", "no vente"
        
def acheter(case, portefeuille, achat, prix):
    achat = "acquerir?"
    if case == 1 and dist(20, 210, mouseX, mouseY)<= 100 and portefeuille > prix:
        portefeuille -= prix
        achat ="achetee"
        return achat, portefeuille
    elif case == 3 and dist(20, 210, mouseX, mouseY)<= 100 and portefeuille > prix:
        portefeuille -= prix
        achat ="achetee"
        return achat, portefeuille
    elif case == 5 and dist(20, 210, mouseX, mouseY)<= 100 and portefeuille > prix:
        portefeuille -= prix
        achat ="achetee"
        return achat, portefeuille
    elif case == 7 and dist(20, 210, mouseX, mouseY)<= 100 and portefeuille > prix:
        portefeuille -= prix
        achat ="achetee"
        return achat, portefeuille
    elif case == 8 and dist(20, 210, mouseX, mouseY)<= 100 and portefeuille > prix:
        portefeuille -= prix
        achat ="achetee"
        return achat, portefeuille
    elif case == 9 and dist(20, 210, mouseX, mouseY)<= 100 and portefeuille > prix:
        portefeuille -= prix
        achat ="achetee"
        return achat, portefeuille
    elif case == 11 and dist(20, 210, mouseX, mouseY)<= 100 and portefeuille > prix:
        portefeuille -= prix
        achat ="achetee"
        return achat, portefeuille
    return achat, portefeuille
    
        

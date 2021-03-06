from random import randint

def saisie(nombre):
    
    if nombre == 1:
        print("Pierre", end=" ") 
        
    elif nombre == 2:
        print("Feuille", end=" ")
        
    elif nombre == 3:
        print("Ciseaux", end=" ")
        
    else:
        print("Fatale error...", end=" ")
        

def maj_scores(bot_chose, player_chose):
    
    global bot_score, player_score 
    
    if bot_chose == 1 and player_chose == 2:
        player_score += 1
    if bot_chose == 1 and player_chose == 3:
        bot_score += 1
        
    if bot_chose == 2 and player_chose == 1:
        bot_score += 1
    if bot_chose == 2 and player_chose == 3:
        player_score += 1
        
    if bot_chose == 3 and player_chose == 1:
        player_score += 1
    if bot_chose == 3 and player_chose == 2:
        bot_score += 1


bot_score = 0
player_score = 0
player_chose = 0

scoreFin = 5

print("Voici chifoumi, est-tu prêt à battre le bot ? car le premier d'entre vous à ", scoreFin, "a gagné !")


while bot_score < scoreFin and player_score < scoreFin:
    while player_chose < 1 or player_chose > 3: # In ne doit pas y avoir d'autres réponses possibles.
        player_chose = int(input("Pierre (1), Feuille (2), Ciseaux (3) : "))
        
    bot_chose = randint(1, 3) #Aléatoirement...
    maj_scores(bot_chose, player_chose)
    print("Tu as choisi", end=" ")
    saisie(player_chose)
    print(" - Le bot à choisi", end=" ")
    saisie(bot_chose)
    print() # Retour à la ligne
    print("Tu as :", player_score, "et le bot à :", bot_score)
    player_chose = 0












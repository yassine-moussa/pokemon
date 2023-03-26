import random 
class Pokemon:
    def __init__(self, name, type1, type2, hp, atk, df, spatk, spdf, spd, move1, move2, move3, move4):
        self.name = name
        self.type1 = type1
        self.type2 = type2
        self.hp = hp
        self.atk = atk
        self.df = df
        self.spatk = spatk
        self.spdf= spdf
        self.spd = spd
        self.move1 = move1
        self.move2 = move2
        self.move3 = move3
        self.move4 = move4
        
class Move:
    def __init__(self, name, form, typ, pwr):
        self.name = name 
        self.form = form
        self.typ = typ
        self.pwr = pwr
        
 
 
Lanceflamme = Move("Lanceflamme", "Special", "Feu", 90)
Tranche = Move("Tranche", "Physique", "Normal", 70)
Lame_dair = Move("Lame d'Air", "Special", "Vol", 75)
Crocs_Feu = Move("Crocs Feu", "Physique","Feu", 65)
Hydro_queue = Move("Hydro Queue", "Physique", "Eau", 90)
Vibraqua = Move("Vibraqua", "Special", "Eau", 60)
Morcure = Move("Morcure", "Physique","Dark", 60)
Tour_rapide = Move("Tour rapide", "Physique", "Normal", 50)
Canon_graine = Move("Canon graine","Physique","Plante",60)
Bombe_Beurk = Move("Bombe Beurk", "Special","Poison", 90)
Coupe_feuille = Move("Coupe feuille", "Physique","Plante", 55)
Damoclès = Move("Damoclès","Physique","Normal", 120)
    
Pok1 = Pokemon("Dracaufeu", "Feu", "Vol", 185, 149, 143, 177, 150, 167, Lanceflamme, Lame_dair, Crocs_Feu, Tranche)
Pok2 = Pokemon("Crocrodile", "Eau", None, 186, 148, 167, 150, 172, 143, Vibraqua, Hydro_queue, Morcure, Tour_rapide)
Pok3 = Pokemon("Méganium", "Plante", "Poison", 187, 147, 148, 167, 167, 145, Canon_graine, Bombe_Beurk, Damoclès, Coupe_feuille)
 
 
 
 
 
def PokAttack(pok1, pok2, move):
    critChance = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1.5]
    randDamage = [85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
    STABdmg = 1
    gamestate = 0  
    if move.typ == pok1.type1:
        STABdmg = 1.5
    elif move.typ == pok1.type2:
        STABdmg = 1.5
    else: pass
 
    dmg = move.pwr
    
    if move.form == "Physique" :
        damage = (((22 * dmg * (pok1.atk / pok2.df)) / 50) + 2) * random.choice (critChance) * (random. choice (randDamage)) * STABdmg
    else:
        damage = (((22 * dmg * (pok1.spatk / pok2.spdf)) / 50) + 2) * random.choice (critChance) * (random .choice (randDamage)) * STABdmg
 
    if move.typ == "Feu" and pok2.type1 == "Eau":    
        damage *= 0.5
    if move.typ == "Feu" and pok2.type1 == "Plante":
        damage *= 1.8
    if move.typ == "Feu" and pok2.type1 == "Feu":
        damage *= 0.5
    if move.typ == "Plante" and pok2.type1 == "Eau":
        damage *= 1.8
    if move.typ == "Plante" and pok2.type1 == "Vol":
        damage *= 0.5
    if move.typ == "Plante" and pok2.type1 == "Plante":
        damage *= 0.5
    if move.typ == "Plante" and pok2.type1 == "Feu":
        damage *= 0.5
    if move.typ == "Eau" and pok2.type1 == "Eau":
        damage *= 0.5
    if move.typ == "Eau" and pok2.type1 == "Plante":
        damage *= 0.5
    if move.typ == "Eau" and pok2.type1== "Feu":
        damage *= 1.8
    if move.typ == "Vol" and pok2.type1 == "Plante":
        damage *= 1.8
 
 
    damage = round(damage,0)
    damage = int(damage/100)
    
    
    print(f'{pok1.name} a utilisé {move.name}')
    pok2.hp -= damage
    print(f"{pok2.name} prend {damage} de dégat !")
        
    if pok2.hp <= 0:
        gamestate = 1
        pok2.hp = 0
            
    print(f'{pok2.name} a {pok2.hp} HP restant. \n')
        
    return gamestate
 
 
party = []
 
pokedex = [Pok1, Pok2, Pok3]
 
print(f'Choisi ton pokemon: (1) {Pok1.name} (2) {Pok2.name} (3) {Pok3.name} ')
 
pokemonChoice = int (input ())
 
if pokemonChoice == 1:
    party.append (Pok1)
   
    print (f"Tu as choisis {Pok1.name}!")
elif pokemonChoice == 2:
    
    party.append (Pok2)
    print(f"Tu as choisis {Pok2.name}!")
elif pokemonChoice == 3:
    party.append (Pok3)
    
    print (f"Tu as choisis {Pok3.name}!")
else:
    choicelol = random.choice (pokedex)
    
    party.append(choicelol)
    
    print (f'Pokemon invalide. Un pokemon aléatoire vous a été attribué... {choicelol.name}.\n')
 
 
 
print(f'Choisis ton adversaire: (1) {Pok1.name} (2) {Pok2.name} (3) {Pok3.name} ')
 
pokemonChoice2 = int (input ())
 
if pokemonChoice2 == 1:
    party.append (Pok1)
   
    print (f"Tu as choisis de combattre {Pok1.name}.")
elif pokemonChoice2 == 2:
    
    party.append (Pok2)
    print(f"Tu as choisis de combattre {Pok2.name}.")
elif pokemonChoice2 == 3:
    party.append (Pok3)
    
    print (f"Tu as choisis de combattre {Pok3.name}.")
else:
    choicelol = random.choice (pokedex)
    
    party.append(choicelol)
    
    print (f'Pokemon invalide. Un pokemon aléatoire a été attribué... {choicelol.name}.\n')
 
 
gamestate = 0
while gamestate == 0:
    if party[0].spd >= party [1].spd:
        print(f"Choisis une attaque: (1) {party[0].move1.name} (2) {party[0].move2.name } (3) {party[0].move3.name} (4) {party[0].move4.name}")
        moveChoice1 = int(input())
        if moveChoice1 == 1:
            if PokAttack(party[0], party[1], party[0].move1) == 1:
                gamestate = 1
        elif moveChoice1 == 2:
            if PokAttack(party[0], party [1], party[0].move2) == 1:
                gamestate = 1
        elif moveChoice1 == 3:
            if PokAttack (party[0], party[1], party [0] .move3) == 1:
                gamestate = 1
        elif moveChoice1 == 4:
            if PokAttack(party[0], party[1], party[0].move4) == 1:
                gamestate = 1 
        if gamestate != 1:
            randMove = random.randint(1,4)
            if randMove == 1:
                if PokAttack (party[1], party[0], party [1] .move1) == 1:
                    gamestate = 2
            elif randMove == 2:
                if PokAttack (party[1], party[0], party [1] .move2) == 1:
                    gamestate = 2
            elif randMove == 3:
                if PokAttack (party[1], party[0], party [1] .move3) == 1:
                    gamestate = 2
            elif randMove == 4:
                if PokAttack (party[1], party[0], party [1] .move4) == 1:
                    gamestate = 2
    else:
        randMove = random.randint(1,4)
        if randMove == 1:
            if PokAttack (party[1], party[0], party [1] .move1) == 1:
                gamestate = 2
        elif randMove == 2:
            if PokAttack (party[1], party[0], party [1] .move2) == 1:
                gamestate = 2
        elif randMove == 3:
            if PokAttack (party[1], party[0], party [1] .move3) == 1:
                gamestate = 2
        elif randMove == 4:
            if PokAttack (party[1], party[0], party [1] .move4) == 1:
                gamestate = 2
        if gamestate != 2:
            print(f"Choisis une attaque: (1) {party[0].move1.name} (2) {party[0].move2.name } (3) {party[0].move3.name} (4) {party[0].move4.name}")
            moveChoice2 = int(input())
            if moveChoice2 == 1:
                if PokAttack(party[0], party[1], party[0].move1) == 1:
                    gamestate = 1
            elif moveChoice2 == 2:
                if PokAttack(party[0], party [1], party[0].move2) == 1:
                    gamestate = 1
            elif moveChoice2 == 3:
                if PokAttack (party[0], party[1], party [0] .move3) == 1:
                    gamestate = 1
            elif moveChoice2 == 4:
                if PokAttack(party[0], party[1], party[0].move4) == 1:
                    gamestate = 1 
    
if gamestate == 1:
    print("Tu as gagné ! Le combat est terminé")
elif gamestate == 2:
    print("Tu as perdu...")
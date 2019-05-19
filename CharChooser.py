#create a basic character by choosing an option and passing a dictionary to a class

import random
import time

BASECHARS = {'b':{'type':"Player",'name':"Barbarian",'attack':3,'defend':2,'move':2,'mind':2,'body':8},
            'w':{'type':"Player",'name':"Wizard",'attack':1,'defend':2,'move':2,'mind':6,'body':4},
            'e':{'type':"Player",'name':"Elf",'attack':2,'defend':2,'move':2,'mind':4,'body':6},
            'd':{'type':"Player",'name':"Dwarf",'attack':2,'defend':2,'move':2,'mind':3,'body':7}}

MONSTERS = {'g':{'type':"Monster",'name':"Goblin",'move':10,'attack':2,'defend':1,'body':1,'mind':1},
            'o':{'type':"Monster",'name':"Orc",'move':8,'attack':3,'defend':2,'body':1,'mind':2},
            'f':{'type':"Monster",'name':"Fimir",'move':6,'attack':3,'defend':3,'body':1,'mind':3},
            's':{'type':"Monster",'name':"Skeleton",'move':6,'attack':2,'defend':2,'body':1,'mind':0},
            'z':{'type':"Monster",'name':"Zombie",'move':4,'attack':2,'defend':3,'body':1,'mind':0},
            'm':{'type':"Monster",'name':"Mummy",'move':4,'attack':3,'defend':4,'body':1,'mind':0},
            'c':{'type':"Monster",'name':"Chaos Warrior",'move':6,'attack':3,'defend':4,'body':1,'mind':3},
            'w':{'type':"Monster",'name':"Warlock",'move':6,'attack':4,'defend':4,'body':1,'mind':4}}

DICE = ('Sword','Sword','Sword','Shield','Shield','Skull')

class Creation(object):
    def __init__(self,Object):
        self.Type = Object['type']
        self.Name = Object['name']
        self.Attack = Object['attack']
        self.Defend = Object['defend']
        self.Move = Object['move']
        self.Mind = Object['mind']
        self.Body = Object['body']

def DiceRoller(numdice):
        myrolls=[]
        if numdice in (1,2,3,4,5):
                for roll in range(0,numdice):
                        myrolls.append(random.choice(DICE))
        else:
                print("Please, numbers 1-5 only: ",numdice)

        return myrolls


def CombatRoller(attacker,defender):
    attroll = DiceRoller(attacker.Attack)
    defroll = DiceRoller(defender.Defend)
    if defender.Type == "Player":
        defense = "Shield"
    else:
        defense = "Skull"
    print("The ",attacker.Name," attacks the ",defender.Name)
    print("Attack: ",attroll, ", Score: ",attroll.count("Sword"))
    print("Defend: ",defroll, ", Score: ",defroll.count(defense))
    if attroll.count("Sword") > defroll.count(defense):
        print("The ",defender.Name," has been wounded")
        defender.Body-=1
    else:
        print("The ",defender.Name," protects themself")

charInput = ''

while charInput not in list(BASECHARS.keys()):
    charInput = input("Pick your character (b/w/e/d): ")
    if BASECHARS.get(charInput):
        myChar = Creation(BASECHARS[charInput])
        print(vars(myChar))
    else:
        print("You didnt pick a valid option")

monsterList = list(MONSTERS.keys())
monstersKilled=0

while myChar.Body>0:
    currMonster = Creation(MONSTERS[random.choice(monsterList)])
    print(vars(currMonster))
    time.sleep(2)
    currentRound = 1

    while myChar.Body > 0 and currMonster.Body > 0:
        print("Round: ",str(currentRound)," ,",currMonster.Name)
        if currentRound%2==1:
            CombatRoller(myChar,currMonster)
        else:
            CombatRoller(currMonster,myChar)
        currentRound+=1
        print(myChar.Name," Health: ",myChar.Body)
        if currMonster.Body == 0:
            monstersKilled+=1

input("Press enter to end")
print("The ",myChar.Name," ended the fights with ",str(myChar.Body)," body and killed a total of ",monstersKilled," monsters")
exit()

from os import remove
import utils

#All covered topics in day one
def testDayOne():
    print('Hello World!')
    utils.line()
    utils.f_string('Juu', 'Roku')
    utils.num
    #The Zen of Python - 20 rules by Tim Peters
    import this
    utils.line()
    list()
    utils.line()

def testDayTwo():
    """This is a docstring for documentation"""
    tuple()
    ifin()
    dict()
    loopAndInput()

def list():
    Tanks_OW = ['D.Va', 'Orisa', 'Sigma', 'Reinhardt', 'Roadhog', 'Winston', 'Wrecking Ball', 'Zarya']
    print(Tanks_OW[-1]+ " is too broken!")
    Tanks_OW[6] = "HamBall"
    #Tanks_OW.append = "Junker Queen"
    Tanks_OW.insert(0, "Doomfist")
    sorted(Tanks_OW, reverse=True)
    Tanks_OW.sort(reverse=True)
    Tanks_OW.reverse()
    len(Tanks_OW)
    """
    String - upper, lower, title
    .remove('Doomfist')
    del Tanks_OW[0]
    .pop()
    .pop(6)
    """
    for tanks in Tanks_OW:
        print(tanks)
    goodTanks = (range(1, len(Tanks_OW)+1), 2)
    for tanks in goodTanks:
        print(tanks)
    HealersOW = [healer//2 for healer in range(1,9)]
    """
    HealersOW[1:3]
    HealersOW[:7]
    HealersOW[-2:]
    copyHealersOW = HealersOW[:]
    """
    for healer in HealersOW[:3]:
        print(healer)

    tuple()

def tuple():
    dpsOW = ('Ashe', 'Bastion', 'Doomfist', 'Genji', 'Hanzo', 'Junkrat', 'McCree', 'Mei', 'Pharah', 'Reaper', 'Soldier: 76', 'Sombra', 'Symmetra', 'Torbjorn', 'Tracer', 'Widowmaker')
    #reachMaster = (1,)
    #static/constant
    
def ifin():
    """
    and
    or
    """
    requestedRoles = ['DPS', 'Tank', 'Healer']
    'DPS' in requestedRoles
    if 'Dev' not in requestedRoles:
        print("Devs shouldn't cheat!")
    overwatchPlayer = True

def dict():
    genjiCharacter = {'health': 200, 'armor': 0, 'speed': 25, 'damage': 25, 'ult': 'Dragonblade'}
    print(genjiCharacter['ult'])
    del genjiCharacter['ult']
    genjiCharacter.get('ult', 'No ult')
    for k,v in genjiCharacter.items:
        print(f"{k}: {v}")
    for keys in sorted(genjiCharacter.keys()):
        print(keys)
    for values in genjiCharacter.values():
        print(values)
    #Set - unique values
    for vals in set(genjiCharacter.values()):
        print(vals)
    alsoASet = {'genji', 'cassidy', 'ashe', 'ana'}

def loopAndInput():
    userRolePreference = input("What role do you want to play?")
    userId = int(input("What is your user ID?"))
    """
    % - modulo - remainder
    break
    continue
    """
    while message != 'leave':
        message = input("Enter 'leave' to exit: ")
        print(message)

testDayTwo()
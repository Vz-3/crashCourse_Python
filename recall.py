from os import *
#from help import variable, datatypes, styling
import utils as u

#All covered topics in day one
def testDayOne():
    print('Hello World!')
    u.line()
    u.f_string('Juu', 'Roku')
    u.num
    #The Zen of Python - 20 rules by Tim Peters
    import this
    u.line()
    list()
    u.line()

def testDayTwo():
    """This is a docstring for documentation"""
    tuple()
    ifin()
    dict()
    loopAndInput()

def testDayThree():
    method()
    classes()
    filed()
    exceptions()
    testingCode()

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
        
def method():    
    def skill(duration, cooldown=3):
        print("Applying {duration} seconds followed by a {cooldown} cooldown")
        #keyword arguments: skill(cooldown=10, duration=5)

    def damageCalculation(heroName, enemy, damage=0, damageType="physical"):
        print(f"{heroName} deals {damage} {damageType} damage to {enemy}")
        calculatedDamage = (damage * 1.5)//2
        return calculatedDamage
    #optional parameter - def damageCalculation(heroName, enemy, damage=0, damageType='') or None

    #slice notation for sending copy of list - skill(durationList[:])
    
    #arbitrary number of arguments
    def enemiesCount(*enemy):
        for enemies in enemy:
            print(enemy)
    #arbitrary number of keyword arguments
    def user_profile(blizardTag, userLevel, **kwargs):
        kwargs['blizardTag'] = blizardTag
        kwargs['userLevel'] = userLevel
        return kwargs
    #thisUser = user_profile(Vzzz#6201, 396, region='NA', role='DPS', hero='Genji')

def classes():
    class OverwatchHero():
        def __init__(self, heroName, heroRole, heroDamage, heroUlt):
            self.heroName = heroName
            self.heroRole = heroRole
            self.heroDamage = heroDamage
            self.heroUlt = heroUlt
        def heroDescription(self):
            print(f"{self.heroName} is a {self.heroRole} with {self.heroDamage} damage and {self.heroUlt} ultimate.")
        def heroUltimate(self):
            print(f"{self.heroName}'s ultimate is {self.heroUlt}.")

    class OverwatchTank(OverwatchHero):
        def __init__(self, heroName, heroRole, heroDamage, heroUlt, heroArmor):
            super().__init__(heroName, heroRole, heroDamage, heroUlt)
            self.heroArmor = heroArmor
            self.ultCharge = 0 #
        def heroDescription(self):
            print(f"{self.heroName} is a {self.heroRole} with {self.heroDamage} damage, {self.heroUlt} ultimate, and {self.heroArmor} armor.")
        def heroUltimate(self):
            print(f"{self.heroName}'s ultimate is {self.heroUlt}.")

    class OverwatchHealer(OverwatchHero):
        def __init__(self, heroName, heroRole, heroDamage, heroUlt, heroHealing):
            super().__init__(heroName, heroRole, heroDamage, heroUlt)
            self.heroHealing = heroHealing
        def heroDescription(self):
            print(f"{self.heroName} is a {self.heroRole} with {self.heroDamage} damage, {self.heroUlt} ultimate, and {self.heroHealing} healing.")
        def heroUltimate(self):
            print(f"{self.heroName}'s ultimate is {self.heroUlt}.")

    class OverwatchDPS(OverwatchHero):
        def __init__(self, heroName, heroRole, heroDamage, heroUlt, heroSpeed):
            super().__init__(heroName, heroRole, heroDamage, heroUlt)
            self.heroSpeed = heroSpeed
        def heroDescription(self):
            print(f"{self.heroName} is a {self.heroRole} with {self.heroDamage} damage, {self.heroUlt} ultimate, and {self.heroSpeed} speed.")
        def heroUltimate(self):
            print(f"{self.heroName}'s ultimate is {self.heroUlt}.")
        #instances as attributes - self.gameChar = OverwatchHero('Genji', 'DPS', 25, 'Dragonblade')

def filed():
    """reading from file"""
    #with is a keyword that closes the file when it is no longer needed
    try:
        with open('test.txt') as file: #looks at the location of 'file'
            contents = file.read()
            print(contents.rstrip()) #rstrip() removes the extra line
    except FileNotFoundError:
        print("File not found.")
    else:
        print(contents)
    finally:
        print("This is the end of the program.")

    def FilePath():
        with open('subFolderUnderThisDirectory/test.txt') as file:
            contents = file.read()
            print(contents.rstrip())
    
    def AbsoluteFilePath():
        file_path = 'C:/Users/V/Documents/crashCoursePython/test.txt' #for backlashes, use double backslashes 'C:\\Users\\V\\Documents\\crashCoursePython\\test.txt'
        with open(file_path) as file:
            contents = file.read()
            print(contents.rstrip())

    def storeDataInList():
        with open('test.txt') as file:
            lines = file.readlines() #readlines stores the lines in a list
        for line in lines:
            print(line.rstrip())

    #replace
    text = "This is the end"
    text.replace('end', 'beginning')

    """writing to file"""
    with open('test.txt', 'w') as file: #w - write, r - read, a - append mode, r+ read and write, read-only by default
        file.write("This is the end.")

def exceptions():
    try:
        print(5/0)
    except ZeroDivisionError:
        print("Zero doesn't exist")
    else:
        print("This is the end of the program.") #additional code after succesful try block

def storingData():
    def json():
        import json
        healingInThousands = [6, 4, 7, 14, 12, 10]
        filename = 'stats.json'
        with open(filename, 'w') as file:
            json.dump(healingInThousands, file)
        
        with open(filename) as file:
            healingInThousands = json.load(file)

def testingCode():
    import unittest
    class RandomTestCase(unittest.TestCase):
        def test(self):
            self.assertEqual(1, 1)

    if __name__ == '__main__':
        unittest.main()

    def listOfCommonAssert(self, x, y, item):
        self.assertEqual(x, y) #x == y
        self.assertNotEqual(x, y) #x != y
        self.assertTrue(x) #x is True
        self.assertFalse(x) #x is False
        self.assertIn(item, list) #item in list
        self.assertNotIn(item, list) #item not in list

    def setUp(self): #multiple responses ; not clear yet
        self.hero = classes().OverwatchHero('Genji', 'DPS', 25, 'Dragonblade')
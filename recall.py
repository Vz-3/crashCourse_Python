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

def list():
    Tanks_OW = ['D.Va', 'Orisa', 'Sigma', 'Reinhardt', 'Roadhog', 'Winston', 'Wrecking Ball', 'Zarya']
    print(Tanks_OW[-1]+ " is too broken!")
    Tanks_OW[6] = "HamBall"
    Tanks_OW.append = "Junker Queen"
    Tanks_OW.insert(0, "Doomfist")
    sorted(Tanks_OW, reverse=True)
    Tanks_OW.sort(reverse=True)
    Tanks_OW.reverse()
    len(Tanks_OW)
    """
    .remove('Doomfist')
    del Tanks_OW[0]
    .pop()
    .pop(6)
    """
    for tanks in Tanks_OW:
        print(tanks)
    goodTanks = list(range(1, len(Tanks_OW)+1), 2)
    #list comprehension and slicing
    
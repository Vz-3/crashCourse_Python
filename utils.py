#11/1/2022
import help

def line():
    print("--------------------")
#recall exponents
def exp(first, second):
    print(first ** second)
#use f_string to format strings
def f_string(first, last):
    print(f"Good day {first} {last}!")
#recall obsolete format replaced by f_string
def obsolete_format(first, last):
    print('Good day {} {}!'.format(first, last))
#run through number data types in python
def num():
    CONSTANT_PI = 3.14
    exp(1, 6)
    float = 0.1+0.2
    print(float)
    float = 4/2
    print(float)
    float = 4/0.25
    print(float)
    billion = 1_000_00_0_0_00
    print(billion)
    
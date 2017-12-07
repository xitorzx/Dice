import os
import random
#import msvcrt

def num() :
    flag = False
    roll_again = 'yes'
    while roll_again =='yes' or roll_again =='y':
         number = random.randint(1,6)
         print ('Dice number: %d' %(number))
         roll_again = raw_input('Rolling the dice again?')
    

def avg(l):
    return sum(l,0.0)/len(l)

if __name__ =='__main__' :
    print ("end of function")    
    random.seed(None)
    num()
    
    

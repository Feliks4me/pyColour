#import random

def colorIndex():
    print("\033[0;31m give me a bottle of rum!") #red
    print("\033[0;32m give me a bottle of rum!") #green
    print("\033[0;33m give me a bottle of rum!") #brown
    print("\033[0;34m give me a bottle of rum!") #blue
    print("\033[0;35m give me a bottle of rum!") #purple
    print("\033[0;36m give me a bottle of rum!") #cyan
    print("\033[0;37m give me a bottle of rum!") #white
    print()
    print("\033[1;31m give me a bottle of rum!") #lred
    print("\033[1;32m give me a bottle of rum!") #lgreen
    print("\033[1;33m give me a bottle of rum!") #yellow
    print("\033[1;34m give me a bottle of rum!") #lblue
    print("\033[1;35m give me a bottle of rum!") #lpurple
    print("\033[1;36m give me a bottle of rum!") #lcyan
    print("\033[1;37m give me a bottle of rum!") #white



colorDick = dict(red = '\033[0;31m')

colorDick['green'] = '\033[0;32m'
colorDick['brown'] = '\033[0;33m'
colorDick['blue'] = '\033[0;34m'
colorDick['purple'] = '\033[0;35m'
colorDick['cyan'] = '\033[0;36m'
colorDick['white'] = '\033[0;37m'

colorDick['lred'] = '\033[1;31m'
colorDick['lgreen'] = '\033[1;32m'
colorDick['yellow'] = '\033[1;33m'
colorDick['lblue'] = '\033[1;34m'
colorDick['lpurple'] = '\033[1;35m'
colorDick['lcyan'] = '\033[1;36m'
colorDick['white'] = '\033[1;37m'

#   dictionary1 = {"key_name":value} 

#   dictionary2 = dict(key_name = value)
#       dictionary2[key_name] = value --> add data to the dictionary

    #colorDick = {'red':'\033[0;31m'} 



def prt(pick = 'green', message = ''):
    for i in range(5):
        if pick in colorDick:            
                print(colorDick[pick]+message)             
                break

        else:
            err = input('Unknown colour! Please try again.. ')
            if err in colorDick:               
                print(colorDick[err]+message)  
                break


def inp(pick = 'green' , message = ''):
    for i in range(5):
        if pick in colorDick:
            value = input(colorDick[pick]+message)
            return value
            break

        else:
            err = input('Unknown colour! Please try again.. ')
            if err in colorDick:
                value = input(colorDick[err]+message)
                return value
                break

def rand():
    pass

def test123(pick = 'green',name = 'none', message = ''):
    input(colorDick[pick]+message)
    return name


def const(pick = 'green'):
    print(colorDick[pick])

#usage
#import color
#color.prt('red', 'debug')
#demo = color.inp('blue', 'demo?')

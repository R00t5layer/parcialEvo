# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 17:20:00 2020

@author: R00t_5layer
"""

def sawer() :
    import os
    
    os.system("cls")
    
    
    
    print("  _____                    _       ")
    print(" |_   _|                  | |      ")
    print("   | | __ _ _ __ __ _  ___| |_ ___ ")
    print("   | |/ _` | '__/ _` |/ _ \ __/ __|")
    print("   | | (_| | | | (_| |  __/ |_\__ \.")
    print("   \_/\__,_|_|  \__, |\___|\__|___/")
    print("                 __/ |             ")
    print("                |___/              ")
    





#--->

targets = []





# /for add

def forAdd(ipe, descripcion) :
    if len(ipe) == 0 and len(descripcion) == 0 :
        ip = input("Enter the ip ---> ")
        descript = input("Enter the description(can be empty) ---> ")
        
        if len(ip) == 0 :
            print("Ip input can't be empty, please try again!")
            import sys
            sys.exit()
        targets.append([ip,descript])
        
        waiter = input("'y' or 'Y' for enter another target, 'n' o 'N' for exit to principal menu ---> ")
        
        looper(waiter)
    

    
def looper(waiter) :
    
    
    if waiter == 'y' or waiter == 'Y' :
        a = ""
        b = ""
        forAdd(a,b)

    elif waiter == 'n' or waiter == 'N' :
        forShow()

    else :
        print("Incorrect char, try again ---> ")
        waiter2 = input("'y' or 'Y' for enter another target, 'n' o 'N' for exit to principal menu ---> ")
        looper(waiter2)
    
    
#  for add \  
    
    
def forDelete(index) :
    print("delete")
    
    
    
    
def forHelp():
    print("List of arguments...")
    print("    -A : To enter targets!")
    print("    -D : To delete targets!")
    

# / for show

def forShow() :
    for e in targets :
        print("Ip : {0}  -  Description : {1}\n".format(e[0], e[1]))
    
    print("For delete one target put 'ip -delete'")
    print("For add one target put 'ip description -add'")
    index = input("---> ")
    response = index.strip().split(" ")
    if len(response[0]) == 0 :
        print("Hello!")
    #forDelete(index)


# for show \
    
    
def menu() :
    sawer()
    '''
    import sys
    
    args = sys.argv
    
    if len(args) < 2 :
        print("Something was wrong!, please type ' targets.py -H' for help")
        sys.exit()
    elif args[1] == "-A" :
        forAdd()
    elif args[1] == "-D" :
        forDelete()
    elif args[1] == "-H" :
        forHelp()
    '''        
menu()
from time import sleep
from random import randint

#Variable global
estado = 'i'

#Estados
def EDOi(entrada):
    global estado
    print('Estado Inicial')
    #Transiciónes
    sleep(2)
    if entrada == 0:
        estado = 'i'
    if entrada == 1:
        estado = 0
        print(u'Transición hacia 0...')

def EDO0(entrada):
    global estado
    print('Estado 0')
    #Transiciones
    sleep(2)
    if entrada == 0:
        estado = 1
        print(u'Transición hacia 1...')
    if entrada == 1:
        estado = 2
        print(u'Transición hacia 2...')
        
def EDO1(entrada):
    global estado
    print('Estado 1')
    #Transiciones
    sleep(2)
    if entrada == 0:
        estado = 0
        print(u'Transición hacia 0...')
    if entrada == 1:
        estado = 2
        print(u'Transición hacia 2...')

def EDO2(entrada):
    global estado
    print('Estado 2')
    #Transiciones
    sleep(2)
    if entrada == 0:
        estado = 1
        print(u'Transición hacia 1...')
    if entrada == 1:
        estado = 0
        print(u'Transición hacia 0...')

#Finite State Machine (FSM)   
def FSM(entrada):
    global estado
    switch = {
       'i':EDOi,
        0 :EDO0,
        1 :EDO1,
        2 :EDO2,
    }
    func = switch.get(estado, lambda: None)
    return func(entrada)

#Programa Principal
while True:    
 FSM(randint(0,1))
 sleep(2)

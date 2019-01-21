#ejercicio clase.
names = ['Alberto','María','Estela','Celia','Carla','Alicia']
repetir = True
while repetir:
    try:
        position = int(input('Introduce un numerito del 1 al 6:'))
        if position in range(1,7):


            repetir = False
        else:
            repetir = True
    except ValueError:
       repetir = True

def ddg(names,position):

    print('La oca es:',names[position])
    return
ddg(names,position)

#UNivesidad del Valle de GUatemala
#Algortitmos Seccion 10
#Steven Rubio 150044
#Erick Bautista 15192
#Hoja de trabajo 5

#aqui se importan las librerias necesarias para el programa
import random
import simpy

"""
Simulacion de un sistema operativo de tiempo compartido


"""
RANDOM_SEED = 22                #Semilla para el random
Procesos = 25                   # Numero de procesos
INTERVAL_Procesos = 10.0        # Tiempo necesario para realizar procesos
Memoria = 100                   #Capacidad de memoria del procesador

#Definicion de los procesos
def new(env,capacidadP):
    "Se generan los procesos, verificando el espacio en memoria"
    memoriaN= random.randrange(1,10,1): #Espacio de memoria necesario
    if capacidadP.level - capacidadP.capacity < 0:
		#No hay espacio en memoria y necesita esperar
		print('Proceso en espera en %d' % env.now)
		yield env.timeout(10)
		
	else:
	
    ready()
    #Hace cola para esperar un espacio de memoria

            
def ready():
    #El proceso esta listo, pero depende de la atencion del CPU
    contador = random.randrange(1,10,1) #Cantidad de instrucciones a realizar
    #Cuando el CPU se desocupa
    running()
    #De lo contrario espera

def running(contador ):
    #Atiende un proceso por tiempo, el tiempo suficiente para realizar 3 instruccines
    instrucciones a realizar = contador
    #Las instrucciones a realizar se actualizan cada tiempo
    #Si le quedan solo 3 instrucciones por realizar, lo libera rapidamente
    #Posibilidades

    #Terminated: Se realizaron todas las instruccioenes y se sale del sistema
    #Waiting:
    nA = random.randrange(1,10,1) #Se genera un numero al azar entre 1 y 10
    #Ai nA es == 1
    #Pasa a la cola de Waiting y regresa a ready
    #Ready: Si el numero es mayor que 1, regresa a la cola de ready


    
#Inicio de la simulacion
print "  ####################################"
print "  #    	  Hoja de trabajo #5         #"
print "  #              SYMPY               #"
print "  ####################################"
print('Simulacion de procesos')
random.seed(RANDOM_SEED)                #Se crea siempre el mismo random, para poder comparar resultados despues

env = simpy.Environment()                                   #Se crea el ambiente de simulacion
procesador = simpy.Resource(env, capacity = 1)              #Se podra realizar solo un proceso a la vez
capacidadP = simpy.Container(env,Procesos,init=Procesos)    #Uso de container

#Comienza el proceso de ejecucion
env.process(new(env,capacidadP))        #Proceso 
env.run()                               #Se corre la simulacion hasta que no existan mas eventos

# env.now() imprime el tiempo de simulacion actual
#Yield = return
# random.randrange(1,10,1) random entre 1 y 10


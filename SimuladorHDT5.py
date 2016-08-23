#UNivesidad del Valle de GUatemala
#Algortitmos Seccion 10
#Steven Rubio 150044
#Erick Bautista 15192
#Hoja de trabajo 5


import simpy
import random

"""
Simulacion de un sistema operativo de tiempo compartido


"""
RANDOM_SEED = 22                #Semilla para el random
Procesos = 25                   # Numero de procesos
Memoria = 100                   #Capacidad de memoria del procesador
Min_p = 1			#Minima cantidad de instrucciones
Max_p = 10			#Maxima cantidad de instrucciones

#Definicion de los procesos
def function(env, tProceso,codigo,RAM, memoriaNecesaria,cantInstrucciones,IPM):
    
	#Se imprime el tiempo de llegada
        yield env.timeout(tProceso)
        print('Tiempo: %f - %s solicita %d de memoria ram' % (env.now, codigo, memoriaNecesaria))
        tiempo_llegada = env.now
	
    #Se solicita un espacio de memoria de la RAM
        yield RAM.get(memoriaNecesaria)
        print('Tiempo: %f - %s (Solicitud de RAM)%d de RAM,aceptada' % (env.now, codigo, memoriaNecesaria))
	
	#Instrucciones completadas
        cantInstC = 0
        while cantInstC < cantInstrucciones:
        #Nos conectamos a la CPU (Estado Ready)
                with CPU.request() as req:
                        yield req
                        #Obtener el numero de instrucciones a realizar
                        if(cantInstrucciones-cantInstC)>=IPM:
                                #Mas de 3 instrucciones a realizar
                                instEfectuar = IPM

                        else:
                                #Menos de 3 instrucciones a realizar
                                instEfectuar=(cantInstrucciones-cantInstC)
			#Imprimimos el tiempo que se tomara en realizar la instruccion
                        print('Tiempo necesario: %f - %s (ready) cpu %d ' % (env.now, codigo, instEfectuar))
			 #Se toma la cantidad de recursos necesaria
                        yield env.timeout(instEfectuar/IPM)   #Error
			#Actualizamos cantidad de instrucciones realizadas
                        cantInstC += instEfectuar
			 
		#Se genera un random para ver si se atiende el proceso o se pone en espera
                        validador = random.randint(1,2)
                        if validador == 1 and instEfectuar<IPM:
                                with Wait.request() as reqE:
                                        yield reqE
				#Espera el tiempo necesario para hacer otra solicitud
                                yield env.timeout(1)
	
	#Se retornan los recursos a la "memmoria"
        yield RAM.put(memoriaNecesaria)
        print('Fin proceso %f - %s, Utilizo %d de memoria' % (env.now, codigo, memoriaNecesaria))

    
#Inicio de la simulacion
print "  ####################################"
print "  #    	  Hoja de trabajo #5         #"
print "  #              SYMPY               #"
print "  ####################################"
print('Simulacion de procesos')

random.seed(RANDOM_SEED)                	        #Se crea siempre el mismo random, para poder comparar resultados despues
env = simpy.Environment()                               #Se crea el ambiente de simulacion
CPU = simpy.Resource(env, capacity = 1)                 #Se podra realizar solo un proceso a la vez
RAM = simpy.Container(env,init=Memoria,capacity= 100)   #Uso de container, tiene capacidad de 100, y comienza con toda la capacidad
Wait= simpy.Resource(env, capacity = 1)			#Capacidad de cola  
instPM = 3.0           #Intrucciones por minuto CPU
constante = 1

#Creacion de procesos
for i in range(Procesos):
	tProceso = random.expovariate(1.0/constante)
	memoriaNecesaria= random.randint(Min_p,Max_p)  #Memoria a solicitar
	cantInstrucciones= random.randint(Min_p,Max_p) #Intrucciones que necesitaran 
	env.process(function(env, tProceso,'Proceso %d' % i,RAM, memoriaNecesaria,cantInstrucciones,instPM))

#Comienza el proceso de ejecucion
env.run()                               #Se corre la simulacion hasta que no existan mas eventos

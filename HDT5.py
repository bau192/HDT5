import random
import simpy

procesos=25
semilla=22
memoriaRam=100
Mdisponible=100
Mtotal=100

def computador(env,tProceso,memoriaDelProceso,procesos,condicion,cpu,waitting,ram):
	yield env.timeout(tProceso)
	print('Tiempo: %f - %s solicita %d de memoria ram' % (env.now, 1, memoriaDelProceso))
	tiempo_llegada = env.now
	
	yield ram.get(memoriaDelProceso)
	


print "  ####################################"
print "  #    	  Hoja de trabajo #5         #"
print "  #              SYMPY               #"
print "  ####################################"
print ""
print('Simulacion de procesos')
print ""
env = simpy.Environment()
tProceso = random.expovariate(1.0/1)
memoriaDelProceso= random.randint(1,10)
procesos=random.randint(1,10)
condicion=random.randint(1,2)
random.seed(semilla)
cpu=simpy.Resource(env,capacity=1)
waitting=simpy.Resource(env, capacity=1)
ram=simpy.Container(env,Mdisponible,Mtotal)


for i in range(procesos):
	#print "proceso numero" ,i
	env.process(computador(env,tProceso,memoriaDelProceso,procesos,condicion,cpu,waitting,ram))
		
env.run() 

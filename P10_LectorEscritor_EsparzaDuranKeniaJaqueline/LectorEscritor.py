import time
from threading import Thread
import os
import random
velocidad1 = 0
velocidad2 = 0
velocidad3 = 0
velocidad4 = 0

def genNumero():
	numero = random.randint(1, 3)
	if(numero == 1):
		return 0.5
	elif(numero == 2):
		return 1
	else:
		return 2

contador = 0
f = open("texto.txt", "r")
b = open("texto.txt", "r")


class lector1(Thread):
    global contador
    def run(self):
        global velocidad1
        while True:
            print("Hola soy el lector 1 y esto leyendo la linea: " + str(contador))
            print(f.read())
            time.sleep(velocidad1)

class lector2(Thread):
    global contador
    def run(self):
        global velocidad2
        while True:
            print("Hola soy el lector 2 y estoy leyendo la linea: " + str(contador))
            print(b.read())
            time.sleep(velocidad2)

class escritor1(Thread):
    def run(self):
        global a
        global velocidad3
        global contador
        while True:
            print("Hola soy el escritor 1 y agregue texto al libro:")
            a = open("texto.txt", "a+")
            a.write("\n+++++++Esta linea ha sido escrita por el escritor 1 num: "+ str(contador))
            a.close()
            contador += 1
            time.sleep(velocidad3)

class escritor2(Thread):
    def run(self):
        global a
        global velocidad4
        global contador
        while True:
            print("Hola soy el escritor 2 y agregue texto al libro:")
            a = open("texto.txt", "a+")
            a.write("\n+++++++Esta linea ha sido escrita por el escritor 2 num: "+ str(contador))
            a.close()
            contador += 1
            time.sleep(velocidad4)

def main():
    global velocidad1
    global velocidad2
    global velocidad3
    global velocidad4
    velocidad1 = genNumero()
    velocidad2 = genNumero()
    velocidad3 = genNumero()
    velocidad4 = genNumero()
    print(velocidad1,velocidad2,velocidad3,velocidad4)
    os.system("pause")
    
    lectura1 = lector1()
    lectura2 = lector2()
    escrito1 = escritor1()
    escrito2 = escritor2()
    lectura1.start()
    lectura2.start()
    escrito1.start()
    escrito2.start()

main()

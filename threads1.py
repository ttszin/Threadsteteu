# Somando Vetores

import time
import threading
import logging
import random

def soma(vetor1,vetor2,inicio,fim,id,vetor_resultante) -> tuple:
    logging.info("Thread %s: starting", id)
    for i in range(inicio, fim):
        vetor_resultante[i] = vetor1[i] + vetor2[i]
    logging.info("Thread %s: finishing", id)
    return vetor_resultante



def main():
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    logging.info("Main    : before creating thread")

    #Lendo entradas
    num_threads = int(input("Insira o número de Threads a ser utilizada: "))
    tam_vetor = int(input("Insira o tamanho dos vetores: "))

    vetor1 = []
    vetor2 = []

    #Adicionando valores nos vetores
    for i in range(tam_vetor):
        num1 = random.randint(0, 100)
        num2 = random.randint(0, 100)
        vetor1.append(num1)
        vetor2.append(num2)

    threads = []
    
    
    tamanho = len(vetor1)
    vetorc = [0] * tamanho
    #Calculando o número de contas para o número de Threads
    num_contas = tam_vetor//num_threads  #Ignora os restos inicialmente
    
    #Percorre as threads
    for i in range(num_threads):
        #O início é calculado com base na iteração atual e com o número de contas
        inicio = i * num_contas        
        #Se i for igual o número de threads o fim é calculado de uma forma, se for a última thread calcula até o final
        if i != num_threads:
            fim = (i+1)*num_contas
        #Se for a ultima thread pega o resto do tamanho do vetor e calcula
        else:
            fim = tamanho
        
        t = threading.Thread(target=soma, args=(vetor1,vetor2,inicio,fim,i,vetorc))
        logging.info("Main    : before running thread")
        t.start()
        threads.append(t)
        logging.info("Main    : wait for the thread to finish")


    for t in threads:
        t.join
    
    logging.info("Main    : all done")
    print(f"Primeiro vetor: {vetor1}")
    print(f"Segundo vetor: {vetor2}")
    print(f"Vetor resultado: {vetorc}")


if __name__ == "__main__":
    main()
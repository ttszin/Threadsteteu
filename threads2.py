#Somando matrizes

import time
import threading
import logging
import random
import numpy as np

#As threads estão processando a matriz por linhas

def soma(matriz1, matriz2, inicio, fim, id, matriz_resultante):
    logging.info(f"Thread {id}: starting")
    #Percorre as linhas da matriz
    for i in range(inicio, fim):
        #Percorre as colunas da matriz
        for j in range(matriz1.shape[1]):
            matriz_resultante[i, j] = matriz1[i, j] + matriz2[i, j]
    logging.info(f"Thread {id}: finishing")
    return matriz_resultante

def main():
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    logging.info("Main    : before creating threads")

    num_threads = int(input("Insira o número de Threads a ser utilizada: "))
    m = int(input("Insira o número de linhas das matrizes: "))
    n = int(input("Insira o número de colunas das matrizes: "))

    matriz1 = np.random.randint(0, 100, size=(m, n))
    matriz2 = np.random.randint(0, 100, size=(m, n))
    matriz_resultado = np.zeros((m, n))

    # Se há mais threads que linhas, use apenas 'm' threads (uma por linha)
    num_threads = min(num_threads, m)

    threads = []
    num_linhas_por_thread = m // num_threads
    resto = m % num_threads  # Restante das linhas que não foi dividido igualmente

    #Percorre as threads
    for i in range(num_threads):
        inicio = i * num_linhas_por_thread
        fim = inicio + num_linhas_por_thread
        if i == num_threads - 1:
            fim += resto  # A última thread pega todas as linhas restantes
        t = threading.Thread(target=soma, args=(matriz1, matriz2, inicio, fim, i, matriz_resultado))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()  # Chamar join como função para garantir que as threads terminem

    logging.info("Main    : all done")
    print(f"Primeira matriz:\n{matriz1}")
    print(f"Segunda matriz:\n{matriz2}")
    print(f"Matriz resultado:\n{matriz_resultado}")

if __name__ == "__main__":
    main()

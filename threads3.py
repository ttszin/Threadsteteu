#Matriz transposta

import time
import threading
import logging
import random
import numpy as np

#As threads estão processando a matriz por linhas

def transposta(matriz, inicio, fim, id, matriz_transposta):
    print(f"inicio: {inicio}\nfim: {fim}")
    logging.info(f"Thread {id}: starting")
    #Percorre as linhas da matriz
    for i in range(inicio, fim):
        #Percorre as colunas da matriz
        for j in range(matriz.shape[1]):
            matriz_transposta[j,i] = matriz[i,j]
    logging.info(f"Thread {id}: finishing")
    return matriz_transposta

def main():
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    logging.info("Main    : before creating threads")

    num_threads = int(input("Insira o número de Threads a ser utilizada: "))
    m = int(input("Insira o número de linhas da matriz: "))
    n = int(input("Insira o número de colunas da matriz: "))

    matriz = np.random.randint(0, 100, size=(m, n))
    matriz_transposta = np.zeros((n, m))

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
        t = threading.Thread(target=transposta, args=(matriz, inicio, fim, i, matriz_transposta))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()  # Chamar join como função para garantir que as threads terminem

    logging.info("Main    : all done")
    print(f"Matriz:\n{matriz}")
    print(f"Matriz Transposta:\n{matriz_transposta}")

if __name__ == "__main__":
    main()

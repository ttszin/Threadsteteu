import os
import threading
from collections import Counter

# Função para calcular as estatísticas de um arquivo
def calcular_estatisticas(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read().lower()

    words = text.split()
    vogais = 'aeiou'
    consoantes = 'bcdfghjklmnpqrstvwxyz'

    # Contar palavras, vogais e consoantes
    word_count = len(words)
    vowel_count = sum(text.count(v) for v in vogais)
    consonant_count = sum(text.count(c) for c in consoantes)
    
    # Encontrar a palavra mais frequente
    word_freq = Counter(words)
    most_common_word, _ = word_freq.most_common(1)[0]

    # Encontrar a vogal mais frequente
    vowel_freq = Counter([char for char in text if char in vogais])
    most_common_vowel, _ = vowel_freq.most_common(1)[0]

    # Encontrar a consoante mais frequente
    consonant_freq = Counter([char for char in text if char in consoantes])
    most_common_consonant, _ = consonant_freq.most_common(1)[0]

    # Print as estatísticas (ou retornar se desejar usar em outro lugar)
    print(f'Estatísticas para {file_path}:')
    print(f'Número de palavras: {word_count}')
    print(f'Número de vogais: {vowel_count}')
    print(f'Número de consoantes: {consonant_count}')
    print(f'Palavra mais frequente: {most_common_word}')
    print(f'Vogal mais frequente: {most_common_vowel}')
    print(f'Consoante mais frequente: {most_common_consonant}')
    print('-' * 40)
    
    # Gerar novo arquivo com conteúdo em maiúsculas
    novo_arquivo = file_path.replace('.txt', '_uppercase.txt')
    with open(novo_arquivo, 'w', encoding='utf-8') as file:
        file.write(text.upper())

# Função que será executada por cada thread
def processar_arquivo(file_path):
    calcular_estatisticas(file_path)

# Função principal para percorrer os arquivos de um diretório e criar threads
def processar_diretorio(directory):
    threads = []
    for file_name in os.listdir(directory):
        if file_name.endswith('.txt'):
            file_path = os.path.join(directory, file_name)
            thread = threading.Thread(target=processar_arquivo, args=(file_path,))
            threads.append(thread)
            thread.start()

    # Aguarde todas as threads terminarem
    for thread in threads:
        thread.join()

# Exemplo de uso
if __name__ == "__main__":
    diretorio = "caminho/do/seu/diretorio"
    processar_diretorio(diretorio)

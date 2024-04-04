import freq

def findKey(ciphertext, min_key_length=1):
    """
    Break Vigenère cipher using Index of Coincidence (IC).
    """
    print("Procurando chave")
    best_ic = 0
    best_key_length = 1
    max_key_length = 20

    #var para armazenar char mais frequente no ciphertext
    most_common_char_ciphertext = freq.freqList(ciphertext)[0][0]
        
    # Descobrindo provável tamanho da chave
    for i in range(min_key_length, max_key_length + 1):
        substrings = [ciphertext[j::i] for j in range(i)]  # Dividindo o texto em substrings de acordo com o tamanho da chave
        ic_sum = 0
        for substring in substrings:
            ic_sum += freq.ic(substring, debug=False)  # Adicionado parâmetro debug=False
        ic = round(ic_sum / i, 3)  # Média das frequências
        print(f"IC para chave de tamanho {i}: {ic}")
        x = abs(ic - 0.072)
        y = abs(best_ic - 0.072)
        if x < y:
            best_ic = ic
            best_key_length = i

    print(f"Melhor tamanho de chave encontrado: {best_key_length}")
    
    # Quebrar o texto em substrings de acordo com o tamanho da chave
    print("\nQuebrando texto em substrings")
    substrings = ['' for _ in range(best_key_length)]
    progresso = 0
    for i, c in enumerate(ciphertext):
        print(f"Progresso: {progresso:.2f}%", end='\r', flush=True)
        substrings[i % best_key_length] += c
        progresso = (i + 1) / len(ciphertext) * 100


    # Calculando frequência de letras e determinando a letra mais frequente para cada substring
    # com isso, calcular a distância para a mais frequente da cifra
    # depois, deslocar a distância equivalente para pegar a chave de verdade
    print("\nCalculando frequência de letras")
    key = ''
    for substring in substrings:
        freqs = freq.freqList(substring)  # Adicionado parâmetro debug=False
        if isinstance(freqs, float):  # Verifica se freqs é um float
            print("Erro: Frequência retornou como float.")
            # convertendo para poder realizar a comparação
            freqs = [freqs]

            continue
        most_common_char_index = freqs.index(max(freqs))
        most_common_char = chr(most_common_char_index + ord('A'))  # Convertendo para caractere
        
        # Calculando distância da most_common_char para most_common_char_ciphertext
        distance = (ord(most_common_char) - ord(most_common_char_ciphertext)) % 26

        # deslocando a distância equivalente para pegar a chave de verdade
        key += chr((ord('A') + distance) % 26)         



    print(f"\nChave encontrada: {key}")

    return key
def breakWithKey(ciphertext, key):
    """
    Break Vigenère cipher using a given key.
    """
    print("\nIniciando quebra de chave")
    print(f"Chave fornecida: {key}")
    print("\nQuebrando cifra em substrings")

    # Quebrar o texto em substrings de acordo com o tamanho da chave
    substrings = ['' for _ in range(len(key))]

    progresso = 0
    total_chars = len(ciphertext)
    for i, c in enumerate(ciphertext):
        print(f"Progresso: {progresso / total_chars * 100:.2f}%", end='\r', flush=True)
        substrings[i % len(key)] += c
        progresso += 1

    print("\nDescriptografando texto")

    plaintext = ''
    progresso = 0
    for i, substring in enumerate(substrings):
        for j, c in enumerate(substring):
            plaintext += chr((ord(c) - ord(key[j % len(key)]) + 26) % 26 + ord('A'))
            progresso += 1
            print(f"Progresso: {progresso / total_chars * 100:.2f}%", end='\r', flush=True)

    print("\nTexto descriptografado:")
    print(plaintext)
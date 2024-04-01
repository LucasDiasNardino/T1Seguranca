import freq

def findKey(ciphertext, min_key_length=1):
    """
    Break Vigenère cipher using Index of Coincidence (IC).
    """
    print("Iniciando quebra de chave")
    best_ic = 0
    best_key_length = 1
    max_key_length = 20
        
    # Descobrindo provável tamanho da chave
    for i in range(min_key_length, max_key_length + 1):
        substrings = [ciphertext[j::i] for j in range(i)]  # Dividindo o texto em substrings de acordo com o tamanho da chave
        ic_sum = 0
        for substring in substrings:
            ic_sum += freq.ic(substring, debug=False)  # Adicionado parâmetro debug=False
        ic = ic_sum / i  # Média das frequências
        print(f"IC para chave de tamanho {i}: {ic}")
        if abs(ic - 0.065) < abs(best_ic - 0.065):
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
        key += most_common_char

    print(f"\nChave encontrada: {key}")

    return key

def breakWithKey(ciphertext, key):
    """
    Break Vigenère cipher using a given key.
    """
    print("\nIniciando quebra de chave")
    print(f"Chave fornecida: {key}")
    print("\nQuebrando texto em substrings")
    substrings = ['' for _ in range(len(key))]
    progresso = 0
    for i, c in enumerate(ciphertext):
        print(f"Progresso: {progresso:.2f}%", end='\r', flush=True)
        substrings[i % len(key)] += c
        progresso = (i + 1) / len(ciphertext) * 100

    print("\nCalculando frequência de letras")
    plaintext = ''
    for i, substring in enumerate(substrings):
        key_char = key[i]
        key_char_index = ord(key_char) - ord('A')
        for c in substring:
            c_index = ord(c) - ord('A')
            plaintext += chr((c_index - key_char_index) % 26 + ord('A'))

    print(f"Texto decifrado:\n{plaintext}")
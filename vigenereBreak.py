import freq

def findKey(ciphertext, min_key_length=1):
    """
    Break Vigenère cipher using Index of Coincidence (IC).
    """
    print("Procurando chave")
    best_ic = 0
    best_key_length = 1
    max_key_length = 20

    # Frequência de letras no idioma português
    freq_portuguese = {
        'a': 0.1463, 'b': 0.0104, 'c': 0.0388, 'd': 0.0499, 'e': 0.1257,
        'f': 0.0102, 'g': 0.0130, 'h': 0.0077, 'i': 0.0618, 'j': 0.0040,
        'k': 0.0002, 'l': 0.0278, 'm': 0.0474, 'n': 0.0505, 'o': 0.1073,
        'p': 0.0252, 'q': 0.0120, 'r': 0.0653, 's': 0.0781, 't': 0.0434,
        'u': 0.0463, 'v': 0.0167, 'w': 0.0001, 'x': 0.0021, 'y': 0.0001,
        'z': 0.0047
    }

    # Var para armazenar char mais frequente no ciphertext
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
    # Com isso, calcular a distância para a mais frequente da cifra
    # Depois, deslocar a distância equivalente para pegar a chave de verdade

    # Calculando frequencia de letras das substrings, e determinando a letra mais frequente
    print("\nCalculando frequência de letras das substrings")
    most_common_char_substrings = []
    for i, substring in enumerate(substrings):
        most_common_char_substrings.append(freq.freqList(substring)[0][0])

    # Concatenando as letras mais frequentes das substrings para formar a chave cifrada
    chaveCifrada = ''.join(most_common_char_substrings)
    print("Chave cifrada: ", chaveCifrada)    

    # Decifrar a chave
    chaveDecifrada = ''
    for char in chaveCifrada:
        shift = ord(char) - ord(most_common_char_ciphertext)
        chaveDecifrada += chr((26 + shift) % 26 + ord('A'))

    print("Chave decifrada: ", chaveDecifrada)

    return chaveDecifrada
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
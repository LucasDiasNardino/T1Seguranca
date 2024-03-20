import freq



def breakVigenere(ciphertext, min_key_length=1,):
    """
    Break Vigenère cipher using Index of Coincidence (IC).
    """
    print("Iniciando quebra de chave")
    best_ic = 0
    best_key_length = 1
    max_key_length = 20
    
    best_ic = freq.ic(ciphertext)
    
    for i in range(min_key_length, max_key_length + 1):
        substring = [ciphertext[j] for j in range(0, len(ciphertext), i)]
        ic = freq.ic(''.join(substring))
        print(f"IC para chave de tamanho {i}: {ic}")
        if abs(ic - 0.065) < abs(best_ic - 0.065):
            best_ic = ic
            best_key_length = i
        

    print(f"Melhor tamanho de chave encontrado: {best_key_length}")
    
    # Split ciphertext into groups based on the guessed key length
    groups = ['' for _ in range(best_key_length)]
    for i, char in enumerate(ciphertext):
        groups[i % best_key_length] += char

    # Perform frequency analysis for each group
    possible_keys = []
    for group in groups:
        frequency = {char: group.count(char) for char in set(group)}
        most_common_char = max(frequency, key=frequency.get)
        possible_keys.append(chr((ord(most_common_char) - ord('a') + 26 - ord('e')) % 26 + ord('a')))

    print("Possíveis chaves encontradas:")
    print(possible_keys)

    # Combine possible keys to form the actual key
    key = ''.join(possible_keys)

    # Decrypt the ciphertext using the key
    plaintext = ''
    for i, char in enumerate(ciphertext):
        shift = ord(key[i % best_key_length]) - ord('a')
        if char.isalpha():
            if char.islower():
                plaintext += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            else:
                plaintext += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
        else:
            plaintext += char

    print( key, plaintext)

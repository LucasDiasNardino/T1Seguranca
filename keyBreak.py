import freq

def breakKey(text):
    #find the key length 
    best_ic = 0
    best_key_length = 1

    for key_length in range(1, text.__len__()):
        groups = ['' for _ in range(key_length)]
        for i, char in enumerate(text):
            groups[i % key_length] += char
        ic = sum(freq.ic(group) for group in groups) / key_length
        if ic > best_ic:
            best_ic = ic
            best_key_length = key_length

    # Split ciphertext into groups based on the guessed key length
    groups = ['' for _ in range(best_key_length)]
    for i, char in enumerate(text):
        groups[i % best_key_length] += char

    # Perform frequency analysis for each group
    possible_keys = []
    for group in groups:
        frequency = {char: group.count(char) for char in set(group)}
        most_common_char = max(frequency, key=frequency.get)
        possible_keys.append(chr((ord(most_common_char) - ord('a') + 26 - ord('e')) % 26 + ord('a')))
                             
    # Combine possible keys to form the actual key
    key = ''.join(possible_keys)

    return key         

import os

def ic(texto,debug=False):

    # calcula a frequencia de cada letra do texto
    freq = {}

    for letra in texto:
        if letra in freq:
            freq[letra] += 1
        else:
            freq[letra] = 1

    # ordena as letras por frequencia
    freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

    # imprime a frequencia

    if debug:
        for letra, f in freq:
            print(f'{letra}: {f}')


    ic = sum([f[1]*(f[1]-1) for f in freq]) / (len(texto)*(len(texto)-1))

    # retorna ic com 4 casas decimais

    return round(ic, 4)

def freqList(texto):
    # calcula a frequencia de cada letra do texto
    freq = {}

    for letra in texto:
        if letra in freq:
            freq[letra] += 1
        else:
            freq[letra] = 1

    # ordena as letras por frequencia
    freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

    return freq

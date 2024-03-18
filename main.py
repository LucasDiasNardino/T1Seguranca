import os

arquivo = 'arqCifradoEN'

def freq(arquivo, debug):

    try:
        with open(arquivo+".txt", 'r') as f:
            texto = f.read()


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

    except FileNotFoundError:
        print(f'Arquivo {arquivo} não encontrado')
        exit()

    except IOError as e:
        print(f'Erro ao abrir o arquivo {arquivo}: {e}')
        exit()


        
print(freq(arquivo, False))
import freq
import vigenereBreak
import os


# freqArqEn = freq.('arqCifradoEN')

# freqArqPt = freq.freq('arqCifradoPT')

# print('Frequencia de letras em arqCifradoEN: ', freqArqEn*100,"%")

# print('Frequencia de letras em arqCifradoPT: ', freqArqPt*100,"%")


# Especifique o caminho da pasta que deseja iterar
caminho_da_pasta = 'C:\\Users\\lucas\\Desktop\\Facul\\7sem\\seg\\t1\\T1Seguranca\\ciphers'


with open('C:\\Users\\lucas\\Desktop\\Facul\\7sem\\seg\\t1\\T1Seguranca\\arqCifradoEN.txt', 'r') as f:
    texto = f.read() 
    # calcula a frequencia de cada letra do texto

    key = vigenereBreak.findKey(texto)   
    vigenereBreak.breakWithKey(texto, key)


# Verifique se o caminho especificado é de fato uma pasta
if os.path.isdir(caminho_da_pasta):
    # Lista todos os arquivos e pastas dentro do caminho especificado
    arquivos_na_pasta = os.listdir(caminho_da_pasta)
    
    # Itera pelos arquivos na pasta
    for arquivo in arquivos_na_pasta:
        # Concatena o caminho da pasta com o nome do arquivo para obter o caminho completo
        caminho_completo = os.path.join(caminho_da_pasta, arquivo)
        
        # Verifica se o caminho é de fato um arquivo (não uma pasta)
        if os.path.isfile(caminho_completo):

           with open (caminho_completo, 'r') as f:
                texto = f.read() 
                # calcula a frequencia de cada letra do texto

                key = vigenereBreak.findKey(texto)   
                vigenereBreak.breakWithKey(texto, key)
                break         


else:
    print("O caminho especificado não é uma pasta válida.")

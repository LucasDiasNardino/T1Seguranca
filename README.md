# Trabalho 1 | Segurança de Sistemas

## Descrição do Trabalho
A ideia é pegar um texto cifrado, utilizando Vigènere, e descriptografar o texto. 

No Vigenère, a chave é repetida até o tamanho do texto, e cada letra do texto é somada com a letra correspondente da chave, resultando em uma nova letra.

Não se sabe a chave, e nem o texto claro.

### Passo 1
Descobrir o tamanho da chave

- Método de Kasiski 
    - Procura-se pedacinhos iguais de texto cifrado, e calcula-se a distância entre eles. A distância entre eles é um múltiplo do tamanho da chave.

- Método Friedman
  - Calcula-se o índice de coincidência do texto cifrado, e compara-se com o índice de coincidência da língua portuguesa. O índice de coincidência da língua portuguesa é 0.0727. O índice de coincidência do texto cifrado é calculado da seguinte forma:
        - Ic = (n1 * (n1 - 1) + n2 * (n2 - 1) + ... + nk * (nk - 1)) / (n * (n - 1))
        - Onde n é o tamanho do texto, e n1, n2, ..., nk são as frequências de cada letra do alfabeto.


### Passo 2

Descobrir a chave

- Método de Kasiski
    - Com o tamanho da chave, pega-se pedaços do texto cifrado, e calcula-se a frequência de cada letra. Com isso, é possível descobrir a chave.

- Método Friedman
    - Com o tamanho da chave, pega-se pedaços do texto cifrado, e calcula-se a frequência de cada letra. Com isso, é possível descobrir a chave.



### Arquivos Auxiliares
Neste [link](https://en.wikipedia.org/wiki/Letter_frequency), temos um arquivo com frequência de letras em português/Inglês
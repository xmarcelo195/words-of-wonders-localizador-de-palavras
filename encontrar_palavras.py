
# abrir o dicionario txt como lista
size_3 = []
with open(r'dicio\size_3.txt', 'r') as f:
    for palavra in f:
      palavra = palavra.rstrip('\n')
      size_3.append(palavra)

size_4 = []
with open(r'dicio\size_4.txt', 'r') as f:
    for palavra in f:
      palavra = palavra.rstrip('\n')
      size_4.append(palavra)

size_5 = []
with open(r'dicio\size_5.txt', 'r') as f:
    for palavra in f:
      palavra = palavra.rstrip('\n')
      size_4.append(palavra)

size_6 = []
with open(r'dicio\size_6.txt', 'r') as f:
    for palavra in f:
      palavra = palavra.rstrip('\n')
      size_4.append(palavra)

size_7 = []
with open(r'dicio\size_7.txt', 'r') as f:
    for palavra in f:
      palavra = palavra.rstrip('\n')
      size_4.append(palavra)


try:

    while True:
        # listas em branco que receberão as respostas
        letras_3 = []
        letras_4 = []
        letras_5 = []
        letras_6 = []
        letras_7 = []
    
        # input das letras disponiveis
        letras_input = input('digite as letras: ')

        #comparar
        i = 0
        sizes = [size_3, size_4, size_5, size_6, size_7]
        while i<=4:
            for palavra in sizes[i]:
                palavra_comparar = palavra
                letras_comparar = letras_input
                for letra in palavra:
                    if letra in letras_comparar:
                        palavra_comparar = palavra_comparar.replace("{}".format(letra), "", 1)
                        letras_comparar = letras_comparar.replace("{}".format(letra), "", 1)

                if len(palavra_comparar) == 0:
                    if len(palavra) == 3:
                        letras_3.append(palavra)
                    if len(palavra) == 4:
                        letras_4.append(palavra)
                    if len(palavra) == 5:
                        letras_5.append(palavra)
                    if len(palavra) == 6:
                        letras_6.append(palavra)
                    if len(palavra) == 7:
                        letras_7.append(palavra)
            i+=1


        print('Palavras com 3 letras: \n',letras_3,'\n')
        print('Palavras com 4 letras: \n',letras_4,'\n')
        print('Palavras com 5 letras: \n',letras_5,'\n')
        print('Palavras com 6 letras: \n',letras_6,'\n')
        print('Palavras com 7 letras: \n',letras_7,'\n')


except KeyboardInterrupt:
    print('\n')

def inputs():
    chaves = []
    valores = []
    with open('inputs.txt','r') as file:
        linhas = file.readlines()
        lista1 = []
        lista2 = []
        lista3 = []
        #Retirar os nomes e espacos em branco
        for termos in linhas:
            a = termos.startswith('#') 
            b = termos.startswith('ï')
            c = termos.startswith('\n')
            if a or b or c:
                pass
            else:
                lista1.append(termos)
        #Retirar espacos nas variaveis
        for termos in lista1:
            lista2.append(termos.split('\t'))
        #Retirar o enter nas variaveis
        for termos in lista2:
            lista3.append(termos[1].split('\n'))
        #Criando a lista de chaves
        for termos in lista2:
            chaves.append(termos[0])
        #Criando a lista de valores
        for termos in lista3:
            valores.append(float(termos[0]))
    #Transformando em dicionarios
    inputs = dict(zip(chaves,valores))
    return inputs
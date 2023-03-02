import csv

#Abrir o arquivo csv com o modo de leitura
with open('D:\\DEV\\apiPython\\geekuniversity\\megasena.csv', 'r') as arquivo_csv:
    #Criar um objeto reader para ler o arquivo csv
    reader = csv.reader(arquivo_csv)
    
    #Obter todas as linhas do arquivo csv
    linhas = list(reader)
    
    #Percorrer cada coluna
    for coluna in range(len(linhas[0])):
        contador = 0
        igual = True
        
        #Percorrer cada linha
        for i in range(1, len(linhas)):
            #Verificar se o valor na primeira coluna da linha atual é igual ao contador + 1
            if linhas[i][coluna] != str(contador + 1):
                igual = False
                break
            contador += 1
        
        #Imprimir o resultado da verificação
        if igual:
            print(f"A coluna {coluna + 1} é igual ao contador")
        else:
            print(f"A coluna {coluna + 1} não é igual ao contador")

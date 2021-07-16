import os
pasta = './Compras'
dados = open("Dados_Compras.txt",'w')
dados.close()
for diretorio, subpastas, arquivos in os.walk(pasta):
    for arquivo in arquivos: 
        obra = open(os.path.join(os.path.realpath(diretorio), arquivo),"r")
        linhas = obra.readlines()
        for linha in linhas:
            array = linha.split(',')
            for elemento in array:
                dados = open("Dados_Compras.txt",'a')
                dados.write(elemento+"\t")
            dados.write("\n")
            dados.close()
            
        obra.close()

dados = open("Dados_Compras.txt",'r')
linhas = dados.readlines()
for linha in linhas:
    array = linha.split()
    print(array)
    print('\n')
dados.close()
    



    

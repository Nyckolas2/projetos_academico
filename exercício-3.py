
def dimensoesObjeto(): # função do quadro 1
    print("----------Etapa 1 de 3----------")
    while True: #loop  que ira repetir a pergunta caso aja algum erro
        try: # ira tentar executar este código caso aja algum erro o bloco que está no "except" sera executado
            al=int(input("altura(cm):"))
            com=int(input("comprimento(cm):"))
            lar=int(input("largura(cm):"))
            vol=al*com*lar # expressão que multiplica  a altura, comprimento e largura
            if vol<1000: # caso o resultado do vol for menor que 1000
                print("o volume do objeto é:{}".format(vol))
                return 10 #retornará o valor 10 para a variavel "vol"
            elif 1000 <= vol < 10000: 
                print("o volume do objeto é:{}".format(vol)) 
                return 20
            elif 10000 <= vol < 30000:
                print("o volume do objeto é:{}".format(vol)) #
                return 30
            elif 30000 <= vol < 10000: 
                print("o volume do objeto é:{}".format(vol))
                return 50 
            else:
                print("o volume do objeto é:{}".format(vol))
                print("o volume do objeto ultrapassa o limite imposto pela empresa, por favor digite novamente")
        except ValueError : # caso o usuário digite uma letra por exemplo "z" no campo de coleta de dados
            print("você digitou alguma dimensão do objeto com um valor não númerico ")    
      
        
        
def pesoObjeto(): # função do quadro 2
    print("----------Etapa 2 de 3----------")
    while True: #loop  
        try:
            peso=float(input("digite o peso do objeto (kg):")) 
            if peso <= 0.1:  # condições específicas para cada grupo determinado de peso
                return 1
            elif peso < 1:
                return 1.5
            elif peso < 10:
                return 2
            elif peso < 30:
                return 3
            else: # se o peso for maior que todas das condições, esse bloco sera executado
                print ("não aceitamos objeto tão pesados")
        except: # caso o usuario digite algo que não está nos parametros definidos pelo programa
            print("você digitou o peso do objeto com um valor não numérico,tente novamente")
    

def rotaObjeto (): # função do quadro 3
    print("----------Etapa 3 de 3----------")
    print("selecione a rota:")  # opções  de rota
    print("RS - De Rio de Janeiro até São Paulo")
    print("SR - De São Paulo até Rio de Janeiro")
    print("BS - De Brasília até São Paulo")
    print("SB - De São Paulo até Brasília")   
    print("BR - De Brasília até Rio de Janeiro")
    print("RB - Rio de Janeiro até Brasília")
    rota=input("selecione a rota:") # campo onde digita a rota
    while True: # loop
            if(rota=="RS"): #condições especifícadas para cada sigla de rota
                return 1
            elif(rota=="SR"):
                return 1
            elif(rota=="BS"):
                return 1.2
            elif(rota=="SB"):
                return 1.2
            elif(rota=="BR"):
                return 1.5
            elif(rota=="RB"):
                return 1.5
            else: # caso o usuario digite algo que não faz parte da tabela, o loop funcionara da mesma maneira porém não foi necessario usar o bloco "try"
                print("")
            while True: # segundo loop da função que só ira ocorrer se o usuário digitar o algo fora das opções
                print("essa rota não existe ou você digitou em minusculo, por favor tente novamente")
                print("")
                print("selecione a rota:")
                print("RS - De Rio de Janeiro até São Paulo")
                print("SR - De São Paulo até Rio de Janeiro")
                print("BS - De Brasília até São Paulo")
                print("SB - De São Paulo até Brasília")   
                print("BR - De Brasília até Rio de Janeiro")
                print("RB - Rio de Janeiro até Brasília")
                rota=input("selecione a rota:")
                if(rota=="RS"):
                    return 1
                elif(rota=="SR"):
                    return 1
                elif(rota=="BS"):
                    return 1.2
                elif(rota=="SB"):
                    return 1.2
                elif(rota=="BR"):
                    return 1.5
                elif(rota=="RB"):
                    return 1.5
        

print("Bem Vindo a Companhia de Logística de Nyckolas Corrêa Rita")
dim=dimensoesObjeto() #variaveis que armazenam os dados obtidos por cada função
peso=pesoObjeto()
rota=rotaObjeto()
total=dim*peso*rota #expressão para calcular o preço com base nos dados obtidos nas funções
print("total a pagar R$:{}".format(total)) # print do preço
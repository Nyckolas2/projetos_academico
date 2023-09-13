#-----variveis globais-----
lista_peças=[]
codigo=0

#função CadastrarPeça

def cadastrarPeça(codigo):
        print("------------------------------")
        print("código do peça:{}".format(codigo))# informa o código da peça
        nome=input('Nome da Peça:')
        fabricante=input('Nome do Fabricante:')
        valor=float(input('valor da peça:'))
        dic={'codigo': codigo, # adiciona os valores das váriaveis acima em cada item no dicionário
             'nome' : nome,
             'fabricante': fabricante,
             'valor': valor}
        lista_peças.append(dic.copy())
     
#função Consultar
def ConsultarPeça():
    print("------------------------------")
    print("Você selecionou Consultar uma Peça")
    while True:#loop 
        print("escolha a opção desejada:")
        print("1-> Consultar Todas as Peças")
        print("2-> Consultar Peça por Código")
        print("3-> Consultar peça por fabricante")
        print("4-> Retornar")
        res=int(input(">>")) # resposta  para qual peça o usuário deseja
        if res==1:
            print("------------------------------")
            print("voce selecionou Cosultar TODAS as peças")
            for peça in lista_peças: # andara dentro de cada dicionrio na lista 
               print("------------------------------")
               for chave, valor in peça.items(): # mostra as chaves e valor do dicionario no produto
                    print('{}:{}'.format(chave,valor))
        elif res==2:
             print("voce selecionou Cosultar  Peça por Código")
             peça_desejada=int(input("digite o numero do código:"))
             for peça in lista_peças:
                  if peça['codigo']==peça_desejada: # se o valor do código da peça for igual ao da peça código
                        print("--------------------")
                        for chave, valor in peça.items(): # mostra as chaves e valor do dicionario no produto
                                print('{}:{}'.format(chave,valor))
                       
        elif res==3:
            print("voce selecionou Cosultar peça por fabricante")  
            peça_desejada=(input("digite o nome do FABRICANTE da peça:"))
            for peça in lista_peças:
                if peça['fabricante']==peça_desejada: # se o nome do fabricante for igual ao fabricante da peça 
                    print("--------------------")
                    for chave, valor in peça.items(): # mostra as chaves e valor do dicionario no produto
                        print('{}:{}'.format(chave,valor))
        elif res==4:
            return # sair da função 
        else:
             print('opção inválida')


#função Remover
def RemoverPeça():
    print("")
    print("você selecionou a opção Remover peça")
    peça_desejada= int(input("digite o código do produto que vc deseja remover"))
    for peça in lista_peças:
         if peça['codigo'] == peça_desejada: # se o numero da peça for igual o que a peça desejada para ser excluida 
              lista_peças.remove(peça) # remover a peça
              print('produto removido')



#-----Programa Principal ( Main )-----
while True:
        print("------------------------------")
        print("Bem Vindo ao controle de estoque do Nyckolas Corrêa Rita")
        print("")
        print("escolha a opção desejada:")
        print("1-> Cadastrar Peça")
        print("2-> Consultar Peça")
        print("3-> Remover Peça")
        print("4-> Sair")
        res=int(input(">>"))
        if res==1:
            codigo+=1
            cadastrarPeça(codigo)
        elif res==2:
            ConsultarPeça()
        elif res==3:
            RemoverPeça()
        elif res==4:
            print("obrigado")
            break
        else: 
            print('opção inexistente')
            continue
   
print("Bem Vindo a Loja do Nyckolas Corrêa Rita")
print("|---------------------cardápio-----------------------|")
print("")
print("|código |---------|   Descrição   |---------| valor |")
print("")
print("|  100   |         Cachorro Quente           | R$9,00  |")
print("|  101   |         Cachorro Quente-Duplo     | R$11,00 |")
print("|  102   |         X-Egg                     | R$12,00 |")
print("|  103   |         X-Salada                  | R$13,00 |")
print("|  104   |         X-Bacon                   | R$14,00 |")
print("|  105   |         X-Tudo                    | R$17,00 |")
print("|  200   |         Refrigerante Lata         | R$5,00  |")
print("|  201   |         Chá Gelado                | R$4,00  |")
print("")
total=0 #variavel fora do loop para poder guardar a soma dos pedidos
while  True: # loop que ira se repetir caso o usuário digite 1
  prod=int(input("código do produto:")) 
  if(prod==100):# condição para pedido de código  100
    print("você selecionou um Cachorro Quente R$9,00")
    total= total + 9.00 # expressão para acumular o preço dos pedidos fora  do loop
    print("deseja pedir mais alguma coisa?")
    print("1 - Sim")
    print("0 - Não")
    res=int(input(">>"))
    if(res==1): # condição para  se o usuário deseja continuar pedindo ou não
        continue # ira voltar para o começo para que o usuário possa pedir outra coisa
    elif(res==0): # se o usuário digitar 0 significa qu ele não quer comprar mais, assim finalizando o pedido e mostrando o total a ser pago e interrompendo o loop 
      print("Total a ser pago: R$ {}".format(total))  
      break
  elif(prod==101): # a partir daqui são as mesmas expressões mudando somente os valores do código do produto e o seu valor
    print("você selecionou um Cachorro Quente-Duplo R$11,00")
    total= total+11.00
    print("deseja pedir mais alguma coisa?")
    print("1 - Sim")
    print("0 - Não")
    res=int(input(">>"))
    if(res==1):
        continue
    elif(res==0):
      print("Total a ser pago: R$ {}".format(total))  
      break
  elif(prod==102):
    print("você selecionou um X-Egg R$12,00")
    total=total+12
    print("deseja pedir mais alguma coisa?")
    print("1 - Sim")
    print("0 - Não")
    res=int(input(">>"))
    if(res==1):
        continue
    elif(res==0):
      print("Total a ser pago: R$ {}".format(total))  
      break    
  elif(prod==103):
    print("você selecionou um X-Salada R$13,00")
    total=total+13
    print("deseja pedir mais alguma coisa?")
    print("1 - Sim")
    print("0 - Não")
    res=int(input(">>"))
    if(res==1):
        continue
    elif(res==0):
      print("Total a ser pago: R$ {}".format(total))  
      break
  elif(prod==104):
    print("você selecionou um X-Bacon R$14,00")
    total=total+14
    print("deseja pedir mais alguma coisa?")
    print("1 - Sim")
    print("0 - Não")
    res=int(input(">>"))
    if(res==1):
        continue
    elif(res==0):
      print("Total a ser pago: R$ {}".format(total))  
      break
  elif(prod==105):
    print("você selecionou um X-Tudo R$17,00")
    total=total+17.00
    print("deseja pedir mais alguma coisa?")
    print("1 - Sim")
    print("0 - Não")
    res=int(input(">>"))
    if(res==1):
        continue
    elif(res==0):
      print("Total a ser pago: R$ {}".format(total))  
      break
  elif(prod==200):
    print("você selecionou um Refrigerante Lata R$ 5,00")
    total=total+5.00
    print("deseja pedir mais alguma coisa?")
    print("1 - Sim")
    print("0 - Não")
    res=int(input(">>"))
    if(res==1):
        continue
    elif(res==0):
      print("Total a ser pago: R$ {}".format(total))  
      break
  elif(prod==201):
    print("você selecionou um Chá Gelado R$4,00")
    total=total+4.00
    print("deseja pedir mais alguma coisa?")
    print("1 - Sim")
    print("0 - Não")
    res=int(input(">>"))
    if(res==1):
        continue
    elif(res==0):
      print("Total a ser pago: R$ {}".format(total))  
      break
  else: #caso o usuaário digite algo que não esta dentro do cardapio este print aparecerá
     print("opção inválida")
  continue # e o código voltara ao início do loop
            
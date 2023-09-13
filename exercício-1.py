print("Bem Vindo a Loja do Nyckolas Corrêa Rita")
valor=float(input("valor do produto:")) #entrada de valor unitário do produto
qnt=int(input("quantidade:")) #entrada da quantidade de produtos
if(qnt<10):   # condição a ser feita se a quantidade  for até 9 unidades, (no caso sem desconto)
  v=valor*qnt
  print("desconto não aplicado")
  print("total:R${}".format(v))
elif(qnt<100):   # condição a ser feita se a quantidade  for até 99 unidades com o (desconto de 5%)
  por=valor*5/100      #expressão para saber o valor do desconto na unidade
  v_desconto= (valor-por)*qnt  #expressão para para saber o valor total com desconto
  v_sem_desconto=valor*qnt #expressão para saber o valor sem desconto com todas as unidades
  print("valor total sem desconto R$:{:.2f}".format(v_sem_desconto))  #saida do valor sem desconto
  print("valor total com desconto R$:{:.2f}""  (desconto de 5%)".format(v_desconto)) # saida do valor com desconto
elif(qnt<1000):   #condição para o desconto de 10%
  por=valor*10/100
  v_desconto= (valor-por)*qnt
  v_sem_desconto=valor*qnt
  print("valor total sem desconto R$:{:.2f}".format(v_sem_desconto))
  print("valor total com desconto R$:{:.2f}""  (desconto de 10%)".format(v_desconto))
else: # se a quantidade for maior que as citadas nas condições anteriores o (desconto sera de 15%)
  por=valor*15/100
  v_desconto= (valor-por)*qnt
  v_sem_desconto=valor*qnt
  print("valor total sem desconto R$:{:.2f}".format(v_sem_desconto))
  print("valor total com desconto R$:{:.2f}""  (desconto de 15%)".format(v_desconto))
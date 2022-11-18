#Calculadora de pesos ideais

sexo = input("Digite seu sexo: ")
h = float(input("Digite sua altura: "))
pm = (72.7*h) - 58
pf = (62.1*h) - 44.7

if sexo = "Masculino":
  print("Peso ideal masculino: ", pm)  
elif sexo = "Feminino":
    print("Peso ideal feminimo: ", pf)
else:
    print("Digite M ou F no sexo para continuar.")

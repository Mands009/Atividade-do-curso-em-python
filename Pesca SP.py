#Calculadora de exceção de quilos de peixe

pei = float(input("Digite a quantidade de peixes em quilos: "))
exc = float(input("Digite o excesso de quilos de peixes: "))
val = 4
mul = exc * val


if pei <= 50 and exc == 0:
    print("Sua pesca não excedeu o peso máximo")
    print("Peso: ", pei, "KG")
    print("Excesso: ", exc)
    print("Multa: ", mul)
else:
    print("Sua pesca excedeu o peso máximo")
    print("Peso: ", pei, "KG")
    print("Excesso: ", exc)
    print("Multa: ", mul)
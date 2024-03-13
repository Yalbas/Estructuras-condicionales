# Programa para saber si los 2 numeros dados son multiplos

#input
A = int(input("ingrese porfavor un numero"))
B = int(input("ingrese porfavor un numero"))

#processing and auoput
if A%B == 0 or B%A == 0:
    print("los numeros",A,"y",B,"son multiplos")
else:
    print("los numeros",A,"y",B,"no son multiplos")

# Programa para saber en que lugar del plano cartesiano esta X o Y.

# Input
X = int(input("ingrese la coordenada x: "))
Y = int(input("ingrese la coordenada y: "))

# Processing
if X == 0:
    if Y == 0:
        print("Esta en el origen del plano cartesiano(0,0)")
    else:
        print("Estas en el eje Y")
elif Y == 0:
    print("Estas en el eje X")
elif X > 0:
    if Y > 0:
        print("Estas en el cuadrante 1")
    else:
        print("Estas en el cuadrante 4")
elif Y < 0:
    print("Estas en el cuadrante 3")
else:
    print("Estas en el cuadrante 2")

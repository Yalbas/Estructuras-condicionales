from math import*
# programa para  Calcular e imprimir las raíces de la ecuación de segundo grado de coeficientes reales

#imput
a = int(input("porvafor ingrese el numero a :"))
b = int(input("porvafor ingrese el numero b :"))
c = int(input("porvafor ingrese el numero c :"))

#procesing
if a == 0:
    print("No hay ecuacion cuadratica")
else:
    d = b**2 -4*a*c
    if d == 0:
        x1 = -b /2*a
        x2 = x1
        print("los resultados de la operacion son : ", x1, x2,)
    elif d > 0:
        x1 = (-b + sqrt(d))/2*a
        x2 = (-b - sqrt(d))/2*a
        print("los resultado de las operaciuones son :",x1 ,x2,)
    else:
        print("no hay solucion real")

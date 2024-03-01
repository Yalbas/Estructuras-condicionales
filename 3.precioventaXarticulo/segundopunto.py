import math
# Programa para calcular el porcentaje de ganancia de un articulo vendido

# input
Precio_costo = float(input ("Ingrese el valor del producto: "))
Ganancia = 0
Precio_venta = Precio_costo+Ganancia

# processing 

if Precio_costo < 3000:
    Ganancia = Precio_costo *0.15
elif  Precio_costo > 6000:
    Ganancia = Precio_costo *0.25
else:
    Ganancia = 500

Precio_venta = (Precio_costo + Ganancia)
# output
print("El producto tiene un precio final de",Precio_venta,)
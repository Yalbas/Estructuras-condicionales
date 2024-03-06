# Un programa para calcular el costo de agua por m3 

# Input

Gasto_agua = int(input("Digite el gasto de agua en su vivienda: "))

# Processing

if Gasto_agua < 50:
    Pago = 10000
elif Gasto_agua < 200:
    Pago = Gasto_agua*2000
else:
    Pago = Gasto_agua*3000

# Output 

print ("El dinero a pagar por el gasto del agua es: ",Pago,)
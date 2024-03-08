# Un programa para calcular el costo de agua por m3 

# Input

M3 = int(input("Digite el gasto de agua en su vivienda: "))
PRECIO_NORMAL= 10000
# Processing

if M3 < 50:
    PAGO = 0 + PRECIO_NORMAL
elif M3 < 200:
    PAGO = ((M3-50) *2000) +PRECIO_NORMAL
else:
    PAGO = ((M3-50) *3000) +PRECIO_NORMAL

# Output 

print ("El dinero a pagar por el gasto del agua es: ",PAGO,)
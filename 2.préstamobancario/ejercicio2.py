# Programa para verificar si un prestamo puede ser consolidado segun el salario o deudas de la persona

# Input
Salario= int(input("¿Cual es tu salario actual? "))
Deuda= input("¿Tienes alguna tipo de deuda? ")

# Processing
if Salario >= 945200:
    if Deuda == "no":
        print ("Su prestamo a sido aprobado")
    else:
        print ("Su prestamo a sido denegado")
else:
    print ("Su prestamo a sido denegado")

    
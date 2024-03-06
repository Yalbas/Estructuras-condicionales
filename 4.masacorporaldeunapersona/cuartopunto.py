# Programa que calcula el indice de masa corporal "IMC" de una persona por medio de su peso y estatura

# Input

Peso = int(input("Ingrese su peso actual: "))
Estatura = float(input("Ingrese su estatura actual: "))

# Processing

IMC = Peso/Estatura**2

if IMC < 16:
    Resultado = "Criterio de ingreso en hospital"
elif IMC <= 17:
    Resultado = "Infrapeso"
elif IMC <= 18.5:
    Resultado = "Bajo peso"
elif IMC <= 25:
    Resultado = "Peso normal (Saludable)"
elif IMC <= 30:
    Resultado = "Sobrepeso (Obesidad de grado 1)"
elif IMC <= 35:
    Resultado = "Sobrepeso crónico (obesidad de grado 2)"
elif IMC <= 40:
    Resultado = "Obesidad premórbida (obesidad de grado 3)"
elif IMC > 40 :
    Resultado = "Obesidad mórbida (obesidad de grado 4)"

# Output

print("Si IMC es",IMC,"y sus resultados son",Resultado,)
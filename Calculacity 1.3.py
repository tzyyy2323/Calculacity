import time
import sys
import math 
import numpy as np  
from math import sqrt
from sympy import symbols, lambdify
import matplotlib.pyplot as plt


def animacion_intro():
    mensaje = "¡Bienvenido a Calculacity!"
    
    for char in mensaje:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)  # Esta funciona para ajustar la velocidad del texto.


if __name__ == "__main__":
    animacion_intro()
    # Termina la animación, sigue con la otra.

def animacion_cargando(duracion=1):
    barra = "||||||||||||||||||||"
    espacios = "                    "
    
    for _ in range(duracion):
        for i in range(len(barra)):
            sys.stdout.write("\rCargando: [{}] {}%".format(barra[:i] + "*" + espacios[i+1:], i*5))
            sys.stdout.flush()
            time.sleep(0.1)  # Estos valores sirven para ajustar la velocidad.
            
    sys.stdout.write("\rCargando: [{}] 100%\n".format("*" * len(barra)))
    time.sleep(0)  # Espera un segundo antes de mostrar el mensaje de "Cargando".
    sys.stdout.write("\n")
    sys.stdout.write("¡Cargado! Iniciando programa...\n")
    sys.stdout.write("\n")

if __name__ == "__main__":
    animacion_cargando()
    # Termina esta animación

def dibujar_suma(n1, n2, suma):
    suma_ascii = f"""
       {n1}
    +  {n2}
    ------------
       {suma}
    """
    return suma_ascii

def calcular_suma(n1, n2):
    suma = n1 + n2
    return suma

def dibujar_resta(minuendo, sustraendo, resultado):
    resta_ascii = f"""
        {minuendo}
    -  {sustraendo}
    ------------
        {resultado}
    """
    return resta_ascii

def calcular_resta(minuendo, sustraendo):
    resultado = minuendo - sustraendo
    return resultado

def dibujar_multiplicacion(factor1, factor2, resultado):
    multiplicacion_ascii = f"""
       {factor1}
    ×  {factor2}
    ------------
       {resultado}
    """
    return multiplicacion_ascii

def calcular_multiplicacion(factor1, factor2):
    resultado = factor1 * factor2
    return resultado

def dibujar_division(dividendo, divisor, cociente, residuo):
    division_ascii = f"""
         {dividendo}
    ÷    {divisor}
    ---------------
         {cociente}
       +{residuo}/{divisor}
    """
    return division_ascii

def calcular_division(dividendo, divisor):
    cociente = dividendo // divisor
    residuo = dividendo % divisor
    return cociente, residuo

def dibujar_raiz_cuadrada(radical, radicando, resultado):
    raiz_cuadrada_ascii = f"""
     √{radical}({radicando})
    -------------
          {resultado:.3f}
    """
    return raiz_cuadrada_ascii

def calcular_raiz_cuadrada(radicando):
    resultado = sqrt(radicando)
    return resultado


def dibujar_porcentaje(numero, porcentaje, resultado):
    porcentaje_ascii = f"""
    {porcentaje}% de {numero}
-------------------------
    {resultado:.2f}
"""
    return porcentaje_ascii

def calcular_porcentaje(numero, porcentaje):
    resultado = numero * (porcentaje / 100)
    return resultado

def dibujar_ecuacion(A, B, C):
    ecuacion_ascii = f""" 
     -({B}) ± √({B}² - 4*{A}*{C})
    -----------------
        2*{A}
"""
    return ecuacion_ascii
    

def resolver_ecuacion_cuadratica(A, B, C):
    discriminante = B**2 - 4*A*C

    if discriminante < 0:
        return "La solución de la ecuación es con números complejos."
    else:
        x1 = int((-B + sqrt(discriminante)) / (2*A))
        x2 = float((-B - sqrt(discriminante)) / (2*A))
        return f"Las soluciones de la ecuación son: x1 = {x1: .1f}, x2 = {x2: .1f}"

def teorema_pitagoras(a, b):
    c = math.sqrt(a**2 + b**2)
    return c

def representacion_ascii_pitagoras(a, b, c):
    representacion = f"""
           /|
          / |
         /  |
      a /   | c
       /    |
      /     |
     /______|
        b
    """
    return representacion

def calcular_area_cuadrado(lado):
    area = lado * lado
    return area

def calcular_area_rectangulo(largo, ancho):
    area = largo * ancho
    return area

def calcular_area_circulo(radio):
    area = math.pi * radio**2
    return area

def longitud_converter(valor, unidad_origen, unidad_destino):
    # Se definen las relaciones de conversión
    relaciones = {
        'milimetro': 1000,
        'centimetro': 100,
        'decimetro': 10,
        'metro': 1,
        'decametro': 0.1,
        'hectometro': 0.01,
        'kilometro': 0.001,
    }
    
    try:
        # Convertir el valor a metros (unidad base)
        
        valor_en_metros = valor * relaciones[unidad_origen]

        # Convertir de metros a la unidad destino mayor de la unidad
        
        valor_convertido_mayor = valor_en_metros / relaciones[unidad_destino]

        # Convertir de metros a la unidad destino menor de la unidad

        valor_convertido_menor = valor_en_metros * relaciones[unidad_destino]

        return valor_convertido_menor

    except KeyError:
        return "Unidad no reconocida. Por favor, elige entre las que se indicaron previamente."
    
def tiempo_converter(valor_tiempo, unidad_origen_tiempo, unidad_destino_tiempo):
    relaciones = {
        'hora': 1,
        'minuto': 60,
        'segundo': 3600
    }

    try:

        valor_en_segundos = valor_tiempo * relaciones[unidad_origen_tiempo]
        valor_convertido_tiempo = valor_en_segundos / relaciones[unidad_destino_tiempo]

        return valor_convertido_tiempo
    
    except KeyError:
        return "Unidad no reconocida. Por favor, elige entre las que se indicaron previamente."
    

def masa_converter(valor_masa, unidad_origen_masa, unidad_destino_masa):
    
    relaciones = {
        'miligramo': 1000,
        'centigramo': 100,
        'decigramo': 10,
        'gramo': 1,
        'decagramo': 0.1,
        'hectogramo': 0.01,
        'kilogramo': 0.001,
    }

    try:

        valor_en_gramo = valor_masa * relaciones[unidad_origen_masa]
        valor_convertido_mayor_masa = valor_en_gramo / relaciones[unidad_destino_masa]
        valor_convertido_menor_masa = valor_en_gramo * relaciones[unidad_destino_masa]

        return valor_convertido_menor_masa
    
    except KeyError:
        return "Unidad no reconocida. Por favor, elige entre las que se indicaron previamente'."
    

def volumen_converter(valor_volumen, unidad_origen_volumen, unidad_destino_volumen):
    
    relaciones = {
        'mililitro': 1000,
        'centilitro': 100,
        'decilitro': 10,
        'litro': 1,
        'decalitro': 0.1,
        'hectolitro': 0.01,
        'kilolitro': 0.001,
    }

    try:

        valor_en_litro = valor_volumen * relaciones[unidad_origen_volumen]
        valor_convertido_mayor_volumen = valor_en_litro / relaciones[unidad_destino_volumen]
        valor_convertido_menor_volumen = valor_en_litro * relaciones[unidad_destino_volumen]

        return valor_convertido_menor_volumen
    
    
    except KeyError:
        return "Unidad no reconocida. Por favor, elige entre las que se indicaron previamente'."
    

historial_puntos_x = []
historial_puntos_y = []


if __name__ == "__main__":
    print("")
    print("Calculacity 1.3")
    print("")
    
    eleccion = 0
    while eleccion != 13:
        
        print("*" * 80)

        print("""
        Indique la operación a realizar
        
        1- Suma
        2- Resta
        3- Multiplicación
        4- División
        5- Calcular raíz cuadrada
        6- Calcular porcentaje
        7- Calcular fórmula para resolver ecuaciones cuadráticas
        8- Calcular teorema de Pitágoras
        9- Calcular el área de figuras
       10- Conversor de unidades
       11- Representar puntos en el plano cartesiano
       12- Formulario
       13- Créditos
        """)

        print("*" * 80)

        eleccion = int(input())

        if eleccion == 1:
            while True:
                n1s = input("Ingrese el primer sumando: ")
                n2s = input("Ingrese el segundo sumando: ")
                try:
                    n1 = float(n1s)
                    n2 = float(n2s)
                except ValueError:
                    print("Ingrese números válidos.")
                    continue
                resultado = calcular_suma(n1, n2)
                representacion_ascii = dibujar_suma(n1s, n2s, str(resultado))
                print("\nResultado:")
                print(representacion_ascii)
                otra_operacion = input("¿Desea realizar otra suma? (Sí/No): ").lower()
                if otra_operacion != 'si':
                    break

        elif eleccion == 2:
            while True:
                minuendo = float(input("Ingrese el minuendo: "))
                sustraendo = float(input("Ingrese el sustraendo: "))
                resultado_resta = calcular_resta(minuendo, sustraendo)
                representacion_ascii_resta = dibujar_resta(minuendo, sustraendo, resultado_resta)
                print("\nResultado de la Resta:")
                print(representacion_ascii_resta)
                otra_operacion = input("¿Desea realizar otra resta? (Sí/No): ").lower()
                if otra_operacion != 'si':
                    break

        elif eleccion == 3:
            while True:
                factor1 = float(input("Ingrese el primer factor: "))
                factor2 = float(input("Ingrese el segundo factor: "))
                resultado_multiplicacion = calcular_multiplicacion(factor1, factor2)
                representacion_ascii_multiplicacion = dibujar_multiplicacion(factor1, factor2, resultado_multiplicacion)
                print("\nResultado de la Multiplicación:")
                print(representacion_ascii_multiplicacion)
                otra_operacion = input("¿Desea realizar otra multiplicación? (Sí/No): ").lower()
                if otra_operacion != 'si':
                    break

        elif eleccion == 4:
            while True:
                dividendo = float(input("Ingrese el dividendo: "))
                divisor = float(input("Ingrese el divisor: "))
                if divisor == 0:
                    print("Error: No se puede dividir por cero.")
                else:
                    cociente, residuo = calcular_division(dividendo, divisor)
                    representacion_ascii_division = dibujar_division(dividendo, divisor, cociente, residuo)
                    print("\nResultado de la División:")
                    print(representacion_ascii_division)
                otra_operacion = input("¿Desea realizar otra división? (Sí/No): ").lower()
                if otra_operacion != 'si':
                    break

        elif eleccion == 5:
            while True:
                numero = float(input("Ingrese el número para calcular la raíz cuadrada: "))
                try:
                    resultado_raiz_cuadrada = calcular_raiz_cuadrada(numero)
                    representacion_ascii = dibujar_raiz_cuadrada(2, numero, resultado_raiz_cuadrada)
                    print("\nResultado de la Raíz Cuadrada:")
                    print(representacion_ascii)
                except ValueError as e:
                    print(f"Error: {e}")
                otra_operacion = input("¿Desea calcular la raíz cuadrada de otro número? (Sí/No): ").lower()
                if otra_operacion != 'si':
                    break

        elif eleccion == 6:
            while True:
                numero = float(input("Ingrese el número: "))
                porcentaje = float(input("Ingrese el porcentaje: "))
                resultado_porcentaje = calcular_porcentaje(numero, porcentaje)
                representacion_ascii = dibujar_porcentaje(numero, porcentaje, resultado_porcentaje)
                print(f"\n{porcentaje}% de {numero} es igual a: {resultado_porcentaje:.2f}")
                print("\nRepresentación ASCII del Porcentaje:")
                print(representacion_ascii)
                otra_operacion = input("¿Desea calcular otro porcentaje? (Sí/No): ").lower()
                if otra_operacion != 'si':
                    break

        elif eleccion == 7:
            while True:
                A = int(input("Ingrese el coeficiente de la variable cuadrática: "))
                B = int(input("Ingrese el coeficiente de la variable lineal: "))
                C = int(input("Ingrese el término independiente: "))
                print(resolver_ecuacion_cuadratica(A, B, C))
                print(dibujar_ecuacion(A, B, C))
                
                otra_operacion = input("¿Desea resolver otra ecuación cuadrática? (Sí/No): ").lower()
                if otra_operacion != 'si':
                    break
        
        elif eleccion == 8:
            
            while True:
                lado_a = float(input("Ingrese la longitud del lado a: "))
                lado_b = float(input("Ingrese la longitud del lado b: "))

                hipotenusa = teorema_pitagoras(lado_a, lado_b)
                print(f"La longitud de la hipotenusa es: {hipotenusa}")
                print(representacion_ascii_pitagoras(lado_a, lado_b, hipotenusa))
                otra_operacion = input("¿Desea resolver otro teorema de Pitágoras? (Sí/No): ").lower()
                if otra_operacion != 'si':
                    break
        
        elif eleccion ==9:
            
            while True:
                
                print("Calcular Áreas:")
                figura = input("Ingrese la figura (cuadrado, rectangulo, círculo): ").lower()

                if figura == "cuadrado":
                    lado = float(input("Ingrese el lado del cuadrado: "))
                    area_cuadrado = calcular_area_cuadrado(lado)
                    print(f"El área del cuadrado es: {area_cuadrado}")

                elif figura == "rectangulo":
                    largo = float(input("Ingrese el largo del rectángulo: "))
                    ancho = float(input("Ingrese el ancho del rectángulo: "))
                    area_rectangulo = calcular_area_rectangulo(largo, ancho)
                    print(f"El área del rectángulo es: {area_rectangulo}")

                elif figura == "circulo":
                    radio = float(input("Ingrese el radio del círculo: "))
                    area_circulo = calcular_area_circulo(radio)
                    print(f"El área del círculo es: {area_circulo}")

                else:
                    print("Figura no reconocida. Por favor, elija cuadrado, rectangulo o círculo")
                
                otra_operacion = input("¿Desea realizar otra operación para calcular áreas? (Sí/No): ").lower()
                if otra_operacion != 'si':
                    break

        elif eleccion == 10:
            while True:
                
                print("Conversión de unidades")

                medicion = input("Ingrese el tipo de unidad que necesita convertir (metro, litro, gramo, tiempo)")

                if medicion == "metro":

                    valor_ingresado = float(input("Ingresa la longitud: "))
                    unidad_origen = input("Ingresa la unidad de origen (milimetro, centimetro, decimetro, metro, decametro, hectometro, kilometro:").lower()
                    unidad_destino = input("Ingresa la unidad de destino (milimetro, centimetro, decimetro, metro, decametro, hectometro, kilometro:").lower()

                    resultado = longitud_converter(valor_ingresado, unidad_origen, unidad_destino)

                    if type(resultado) == float:
                        print(f"{valor_ingresado} {unidad_origen} es igual a {resultado} {unidad_destino}.")
                    else:
                        print(resultado)
                    
                    otra_operacion = input("¿Desea realizar otra conversión? (Si/No)").lower()
                    if otra_operacion != 'si':
                        break

                elif medicion == "litro":

                    valor_ingresado_volumen = float(input("Ingresa la capacidad: "))
                    unidad_origen_volumen = input("Ingresa la unidad de origen (mililitro, centilitro, decilitro, litro, decalitro, hectolitro, kilolitro):").lower()
                    unidad_destino_volumen = input("Ingresa la unidad de destino (mililitro, centilitro, decilitro, litro, decalitro, hectolitro, kilolitro:").lower()

                    resultado = volumen_converter(valor_ingresado_volumen, unidad_origen_volumen, unidad_destino_volumen)

                    if type(resultado) == float:
                        print(f"{valor_ingresado_volumen} {unidad_origen_volumen} es igual a {resultado} {unidad_destino_volumen}.")
                    else:
                        print(resultado)
                    
                    otra_operacion = input("¿Desea realizar otra conversión? (Si/No)").lower()
                    if otra_operacion != 'si':
                        break
                
                elif medicion == "gramo":

                    valor_ingresado = float(input("Ingresa la masa: "))
                    unidad_origen_masa = input("Ingresa la unidad de origen (miligramo, centigramo, decigramo, gramo, decagramo, hectogramo, kilogramo:").lower()
                    unidad_destino_masa = input("Ingresa la unidad de destino (miligramo, centigramo, decigramo, gramo, decagramo, hectogramo, kilogramo:").lower()

                    resultado = masa_converter(valor_ingresado, unidad_origen_masa, unidad_destino_masa)

                    if type(resultado) == float:
                        print(f"{valor_ingresado} {unidad_origen_masa} es igual a {resultado} {unidad_destino_masa}.")
                    else:
                        print(resultado)
                    
                    otra_operacion = input("¿Desea realizar otra conversión? (Si/No)").lower()
                    if otra_operacion != 'si':
                        break

                elif medicion == "tiempo":

                    valor_ingresado = float(input("Ingresa el tiempo: "))
                    unidad_origen = input("Ingresa la unidad de origen (hora, minuto, segundo): ").lower()
                    unidad_destino = input("Ingresa la unidad de destino (hora, minuto, segundo): ").lower()

                    resultado = tiempo_converter(valor_ingresado, unidad_origen, unidad_destino)

                    if type(resultado) == float:
                        print(f"{valor_ingresado} {unidad_origen} es igual a {resultado} {unidad_destino}.")
                    else:
                        print(resultado)
                    
                    otra_operacion = input("¿Desea realizar otra conversión? (Si/No)").lower()
                    if otra_operacion != 'si':
                        break
        
        elif eleccion == 11:
                        # Pedir al usuario que ingrese la función
            x = symbols('x')
            expresion_funcion = input("Ingresa la expresión de la función en términos de x: ")

            # Crear la función a partir de la expresión ingresada
            try:
                funcion = lambdify(x, expresion_funcion, 'numpy')
            except Exception as e:
                print(f"Error al crear la función: {e}")
                exit()

            # Valores de x de la tabla
            valores_x = [-3, -2, -1, 0, 1, 2, 3]

            # Calcular los valores correspondientes de y utilizando la función ingresada
            valores_y = [funcion(valor_x) for valor_x in valores_x]

            # Dibujar el plano cartesiano con la función
            plt.title('Plano Cartesiano con Función')
            plt.xlabel('Eje X')
            plt.ylabel('Eje Y')

            # Dibujar los ejes X e Y (la cruz)
            plt.axhline(0, color='black', linewidth=2, linestyle='--')
            plt.axvline(0, color='black', linewidth=2, linestyle='--')

            # Mostrar la función
            plt.plot(valores_x, valores_y, color='blue', marker='o', label=f'Función: {expresion_funcion}')

            # Mostrar los puntos en el plano
            plt.scatter(valores_x, valores_y, color='red', marker='o', label='Puntos de la función')

            # Mostrar el gráfico
            plt.grid(True)
            plt.legend()
            plt.show()
                        


        elif eleccion == 12:
                
            while True:
            
                print("*" * 80)

                print("Elija el formulario que desea ver:")
                print("""
                
                      
                      1- Leyes de los exponentes
                      2- Productos notables
                      3- Leyes de los signos
                      4- Movimiento rectilíneo uniforme
                      5- Movimiento rectilíneo uniformemente acelerado
                      6- Movimiento vertical hacia arriba
                      7- Caída libre
                      8- Cerrar el programa
                      
                      """)
                
                print("*" * 80)
                
                opcion_principal = input("Ingrese el número de la opción: ")

                if opcion_principal == "1":
                    
                    print("")
                    print("Multiplicación de potencias con la misma base:")
                    print("a^m * a^n = a^(m + n)")
                    print("")
                    print("División de potencias con la misma base:")
                    print("a^m / a^n = a^(m - n)")
                    print("")
                    print("Potencia de una potencia:")
                    print("(a^m)^n = a^(m * n)")
                    print("")
                    print("Potencia de 0:")
                    print("a^0 = 1 (siempre que a sea diferente de 0)")
                    print("")
                    print("¡Recuerda que estas leyes aplican para bases no negativas!")
                    print("")

                elif opcion_principal == "2":
                    
                    print("")
                    print("Binomio cuadrado perfecto:")
                    print("(a + b)^2")
                    print("")
                    print("Binomio cuadrado perfecto:")
                    print("(a - b)^2")
                    print("")
                    print("Diferencia de cuadrados:")
                    print("(a + b)(a - b)")
                    print("")
                    print("Binomio cubo perfecto:")
                    print("(a + b)^3")
                    print("")
                    print("Binomio cubo perfecto:")
                    print("(a - b)^3")
                    print("")
                    print("Diferencia de cuadrados:")
                    print("a^2 - b^2")
                
                elif opcion_principal == "3":
                    
                    print("")
                    print("Suma de números con mismo signo:")
                    print("""
                    (+a) + (+b) = +c
                    (-a) + (-b) = -c
                    """)
                    print("")
                    print("Suma de números con signos diferentes:")
                    print("""
                    (+a) + (-b) = +c
                    (-a) + (+b) = -c
                    """)
                    print("")
                    print("Resta de números con mismo signo:")
                    print("""
                    (+a) - (+b) = +c
                    (-a) - (-b) = -c
                    """)
                    print("")
                    print("Resta de números con signos diferentes:")
                    print("""
                    (+a) - (-b) = +c
                    (-a) - (+b) = -c
                    """)
                    print("")
                    print("Multiplicación de números con mismo signo:")
                    print("""
                    (+a) * (+b) = +c
                    (-a) * (-b) = +c
                    """)
                    print("")
                    print("Multiplicación de números con signos diferentes:")
                    print("""
                    (+a) * (-b) = -c
                    (-a) * (+b) = -c
                    """)
                    print("")
                    print("División de números con mismo signo:")
                    print("""
                    (+a) / (+b) = +c
                    (-a) / (-b) = +c
                    """)
                    print("")
                    print("División de números con signos diferentes:")
                    print("""
                    (+a) / (-b) = -c
                    (-a) / (+b) = -c
                    """)
            
                elif opcion_principal == "4":

                    print("")
                    print("Calcular distancia")
                    print("d = v * t")
                    print("")
                    print("Calcular velocidad")
                    print("v = d / t")
                    print("")
                
                elif opcion_principal == "5":

                    print("")
                    print("Calcular velocidad final")
                    print("Vo + a * t")
                    print("")
                    print("Calcular aceleración")
                    print("Vf - Vo / t")
                    print("")
                    print("Calcular tiempo")
                    print("Vf - Vo / a")
                    print("")
                    print("Calcular distancia")
                    print("Vo * t + 1/2 a * t^2")
                    print("")
                
                elif opcion_principal == "6":
                    
                    print("")
                    print("Calcular altura")
                    print("Vo * t - (g * t^2 /2)")
                    print("")
                    print("Calcular velocidad final")
                    print("Vo - g * t")
                    print("")
                    print("Calcular velocidad inicial")
                    print("Vf - g * t")
                    print("")
                    print("Calcular altura máxima")
                    print(" - Vo^2 / 2 * g")
                    print("")
                    print("Calcular tiempo máximo")
                    print("- Vo / g")
                    print("")
                    print("Calcular tiempo de vuelo")
                    print("2 * tmax")
                
                elif opcion_principal == "7":

                    print("")
                    print("Calcular velocidad final")
                    print("g * t")
                    print("")
                    print("Calcular tiempo")
                    print("Vf / g")
                    print("")
                    print("Calcular altura")
                    print("g * t^2 / 2")
                
                elif opcion_principal == "8":
                    sys.exit()
            
        elif eleccion == 13:
            
            print("*" * 80)
            print("")
            print("Programa creado por los estudiantes Siugel Chong y Luis Diego Salas")
            print("")
            print("El profesor Ruben Leal como nuestro tutor guía")
            print("")
            print("Unidad Psicoeducativa Julio Chevalier")
            print("")
            print("Reto de matemáticas 2024")
            print("")
            print("*" * 80)

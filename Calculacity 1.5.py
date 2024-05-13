import time
import sys
import math
import os
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
       
        +{residuo}
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

def calcular_trigonometria(angulo_en_grados):
    # Convertir el ángulo de grados a radianes
    angulo_en_radianes = math.radians(angulo_en_grados)
    
    seno = math.sin(angulo_en_radianes)
    coseno = math.cos(angulo_en_radianes)
    
    return seno, coseno

def calcular_tangente(angulo_en_grados):
    # Convertir el ángulo de grados a radianes
    angulo_en_radianes = math.radians(angulo_en_grados)
    
    # Calcular la tangente del ángulo
    tangente = math.tan(angulo_en_radianes)
    
    return tangente

def calcular_modulo_vector_2D(A, B):
    # Calcular las componentes del vector AB
    AB = [B[i] - A[i] for i in range(len(A))]
    
    # Calcular el módulo del vector AB
    modulo = math.sqrt(sum(comp ** 2 for comp in AB))
    
    return modulo

historial_puntos_x = []
historial_puntos_y = []


if __name__ == "__main__":
    print("")
    print("Calculacity 1.5")
    print("")
    
    eleccion = 0
    while eleccion != 14:
        
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
       10- Calcular seno y coseno
       11- Calcular la tangente
       12- Calcular la magnitud de dos vectores
       13- Representar puntos en el plano cartesiano
       14- Glosario
       15- Formulario
       16- Créditos
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

            angulo = float(input("Ingrese el ángulo en grados: "))
            seno, coseno = calcular_trigonometria(angulo)

            print(f"El seno de {angulo} grados es: {seno}")
            print(f"El coseno de {angulo} grados es: {coseno}")
        
        elif eleccion == 11:

            angulo = float(input("Ingrese el ángulo en grados: "))
            tangente = calcular_tangente(angulo)
            print(f"La tangente de {angulo} grados es: {tangente}")

        elif eleccion == 12:

            # Solicitar al usuario el número de vectores
            num_vectores = int(input("Ingrese el número de vectores: "))

            # Inicializar una lista para almacenar los vectores
            vectores = []

            # Solicitar las coordenadas de los vectores
            for i in range(num_vectores):
                coordenadas = input(f"Ingrese las coordenadas del vector {i+1} (separadas por comas, por ejemplo, 'x,y'): ")
                vector = [float(coord) for coord in coordenadas.split(",")]
                vectores.append(vector)

            # Calcular el módulo de cada vector con respecto al primer vector
            primer_vector = vectores[0]
            for i in range(1, num_vectores):
                modulo = calcular_modulo_vector_2D(primer_vector, vectores[i])
                print(f"El módulo del vector {i+1} es:", modulo)


        elif eleccion == 13:
            
            def guardar_grafica(expresion_funcion, valores_x, valores_y):
                # Crear la función a partir de la expresión ingresada
                try:
                    funcion = lambdify(x, expresion_funcion, 'numpy')
                except Exception as e:
                    print(f"Error al crear la función: {e}")
                    return

                # Limpiar la figura antes de dibujar una nueva gráfica
                plt.clf()

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

                # Obtener la ruta del directorio "Mis Documentos"
                directorio_documentos = os.path.join(os.path.expanduser("~"), "Documents", "Documentos")

                # Generar un nombre único para el archivo .png
                nombre_archivo = f'grafica_{expresion_funcion.replace(" ", "_").replace("/", "_").replace("*", "_")}.png'
                archivo_salida = os.path.join(directorio_documentos, nombre_archivo)

                # Guardar la gráfica en el archivo .png
                plt.savefig(archivo_salida)

                # Mostrar un mensaje de confirmación
                print(f"La gráfica se ha guardado en {archivo_salida}")
          
            # Pedir al usuario que ingrese la función
            x = symbols('x')
            expresion_funcion = input("Ingresa la expresión de la función en términos de x: ")

            # Valores de x de la tabla
            valores_x = [-3, -2, -1, 0, 1, 2, 3]

            # Calcular los valores correspondientes de y utilizando la función ingresada
            valores_y = [lambdify(x, expresion_funcion, 'numpy')(valor_x) for valor_x in valores_x]

            # Llamar a la función para guardar y mostrar la gráfica
            guardar_grafica(expresion_funcion, valores_x, valores_y)


        elif eleccion == 14:

            while True:
                  
                    print("*" * 80)

                    print("Elija que materia necesita estudiar:")
                    print("""
                        
                        1- Física
                        2- Matemáticas
                        3- Salir de este menú
                        """)
                    
                    print("*" * 80)
                    
                    opcion_glosario = input("Ingrese el número de la opción:")

                    if opcion_glosario == "1":
                                while True:
                                
                                    print("*" * 80)
                                    print("Elija que tema desea ver")
                                    print("""
                                        1- Conceptos generales
                                        2- Movimiento Rectilíneo Uniforme (MRU)
                                        3- Novimiento Rectilíneo Uniforme Variado (MRUV)
                                        4- Movimiento vertical
                                        """)
                                    
                                    opcion_física = input("Ingrese el número de la opción:")
                                    
                                    if opcion_física == "1":
                                        print("""   
                                        
                                        ¿Qué es la Física?
                                        
                                        - La palabra física proviene del vocablo griego physis, que significa naturaleza.
                                        Mediante la observación de la naturaleza, esta ciencia trata de descubrir las
                                        leyes que rigen la mate ria y la energía en cualquiera de sus formas.
                                        Es una ciencia que ayuda a comprender el comportamiento de los fenómenos
                                        naturales del universo que se desarrollan en el espacio y el tiempo.
                                        La física se ocupa de estudiar las propiedades de la materia, la energía, el
                                        tiempo, el espacio y sus interacciones (fuerzas). La física utiliza el método científico
                                        para formular y probar sus hipótesis.
                                        
                                        2) Sistema Internacional de unidades
                                        
                                        - Las mediciones fiables y exactas exigen unidades inalterables que los
                                        observadores puedan duplicar en distintos lugares. Por tal razón en virtud de un
                                        acuerdo firmado en 1960, se estableció en la mayor parte del mundo, un sistema de
                                        unidades para científicos e ingenieros, denominado “Sistema Internacional de
                                        unidades” (S. I.), Resultado del trabajo de la llamada Conferencia General de Pesos
                                        y Medidas, organización internacional con representación en la mayoría de países.
                                            
                                        3) ¿Qué es un despeje?
                                            
                                        - Es aquella ecuación o fórmula en la que se requiere despejar una variable. Se
                                        entiende por variable una letra o incógnita.
                                            
                                        4) ¿Qué es una fórmula?
                                            
                                        - Es una expresión que relaciona tres o más cantidades.
                                        A las cantidades conocidas que siempre tienen el mismo valor se les llama
                                        constantes. Si por el contrario, los valores de una cantidad pueden cambiar se les
                                        llama variables. Las fórmulas son usadas para hallar el valor de las variables,
                                        usando las variables conocidas y las constantes.
                                            
                                        5) ¿Qué es un radical?
                                        
                                        - Es aquella expresión matemática en la cual uno de sus términos tiene un
                                        radicando (una raíz).
                                            
                                        6) ¿Qué es una cantidad subradical?
                                            
                                        - Es toda aquella que se encuentra dentro de una raíz. Cuando no se vea el índice
                                        de la raíz su valor es 2 (cuadrado).
                                        """)
                                        break
                                    
                                    elif opcion_física == "2":
                                        print("""
                                            
                                        1) ¿Qué es movimiento?
                                        
                                        - Es aquel que realiza un cuerpo desde un punto de inicio hasta un punto final sin
                                        importar su trayectoria.)
                                        
                                        2) ¿Qué es el movimiento rectilíneo uniforme?
                                        
                                        - Es el movimiento que realiza un cuerpo recorriendo distancias iguales en tiempos
                                        iguales y su trayectoria es una línea recta.
                                        En el M.R.U la aceleración es cero (nula).
                                        
                                        Para calcular ese movimiento se requiere la siguiente fórmula:
                                        
                                        v = d/t
                                        
                                        Dónde:
                                        
                                        v = Velocidad
                                        
                                        d = Distancia
                                        
                                        t = Tiempo

                                        3) ¿Qué es velocidad?
                                        
                                        - Se llama como tal al recorrido efectuado por un cuerpo en un tiempo
                                        determinado.
                                        Unidad de medición:
                                        Su unidad derivada es: [metro/segundo] = [m/s]
                                        
                                        4) ¿Qué es distancia?
                                        
                                        - Es la cantidad de espacio recorrido por el móvil en su desplazamiento.
                                        
                                        5) ¿Qué es desplazamiento?
                                        
                                        - Es el segmento dirigido que une dos posiciones diferentes de la trayectoria de
                                        un objeto en movimiento.
                                        
                                        6) ¿Qué es el tiempo?
                                        
                                        - Es la magnitud que sirve para medir la duración o la separación de uno o más
                                        acontecimientos.
                                        """)
                                        break

                                    elif opcion_física == "3":
                                        print("""
                                            
                                        1) ¿Qué es el movimiento rectilíneo uniforme variado?
                                        
                                        - Es aquel movimiento que experimenta un cuerpo cuando es sometido a una
                                        aceleración que permite desplazarlo de un lugar a otro. En este movimiento la V es
                                        variable.
                                        
                                        Para que se produzca el movimiento debe haber una aceleración y para
                                        detenerlo una desaceleración.
                                            
                                        2) ¿Qué es aceleración?
                                        
                                        - Es una magnitud derivada vectorial que nos indica la variación de velocidad por
                                        unidad de tiempo.
                                        
                                        3) ¿Qué se entiende por distancia máxima?

                                        - Es la distancia recorrida durante el tiempo máximo.

                                        4) ¿Qué es el tiempo máximo?

                                        - Es el tiempo que tarda un cuerpo en detenerse.

                                        5) Diferencias entre el movimiento rectilíneo uniforme y el movimiento rectilíneo
                                        uniforme variado 
                                        
                                        - La principal diferencia entre M.R.U y M.R.U.V es la aceleración. En el M.R.U, la
                                        aceleración es nula, mientras que en el M.R.U.V, la aceleración es constante.
                                        Como consecuencia de la diferencia en la aceleración, la velocidad también se
                                        comporta de manera diferente. En el M.R.U, la velocidad es constante, mientras que
                                        en el M.R.U.V, la velocidad varía.
                                        """)
                                        break
                                    
                                    elif opcion_física == "4":
                                        print("""
                                        
                                        1) ¿Qué se entiende por movimiento vertical?
                                            
                                        - Es un movimiento uniforme acelerado en la cual depende de la fuerza de
                                        gravedad. Se clasifica en:Movimiento ascendente: Es aquel que requiere de una velocidad inicial
                                        (obligatoria) para comenzar su movimiento y cuya velocidad final es igual a 0
                                        siempre y cuando no exista algún factor que la detenga en el camino.
                                        Movimiento descendente (Caída Libre): Es un movimiento acelerado hacia abajo
                                        y el cual no requiere de una velocidad inicial previa.
                                        
                                        2) ¿Qué es la gravedad?
                                        
                                        - Es la fuerza con la que un objeto es atraído al centro de la tierra.
                                        En el globo terráqueo la gravedad es igual a 9,8m/s (al cuadrado) y en la luna es
                                        de 1,6 m/s (al cuadrado).
                                        
                                        3) ¿Qué se entiende por peso?
                                            
                                        - Es la proporcionalidad directa entre la masa de un cuerpo y la gravedad.
                                        Se calcula de la siguiente manera: 
                                            
                                        * Peso = Masa x Gravedad / p = m x g.
                                        
                                        4) ¿Qué se entiende por tiempo de vuelo?
                                        
                                        - Es el tiempo que dura el objeto en el aire sin que se interrumpa su movimiento
                                        cuando retorna a su posición inicial.
                                        """)
                                        break
                                
                    elif opcion_glosario == "2":
                                    
                                        print("*" * 80)
                                        print("Elija que tema desea ver")
                                        print("""
                                            1- Conceptos generales
                                            2- Polinomios
                                            3- El Plano Cartesiano o Plano real
                                            4- Sistema de ecuaciones
                                            """)
                                        
                                        opcion_matematicas = input("Ingrese el número de la opción:")
                                
                                        if opcion_matematicas == "1":
                                            print("""
                                                
                                            1) ¿Qué se entiende por números naturales?
                                            
                                            - Es cualquiera de los números que se usan para contar los elementos de ciertos
                                            conjuntos. Se representan con la N = {0, 1, 2, 3, 4,...}. De dos números vecinos, el
                                            que se encuentra a la derecha se llama siguiente o sucesivo, por lo que el conjunto
                                            de los números naturales es ordenado e infinito.
                                            
                                            2) ¿Qué son los números enteros?
                                            - Un número entero es un elemento del conjunto numérico que contiene
                                            los números naturales; que son N = {0, 1, 2, 3, 4,...} o N* = {1, 2, 3, 4,...};
                                            dependiendo de cómo se definan, sus opuestos, y en la segunda definición, además
                                            el cero. Los enteros negativos, son menores que cero y también son menores que
                                            todos los enteros positivos. Para resaltar la diferencia entre positivos y negativos,
                                            se puede escribir un signo «menos» delante de los negativos. Y si no se escribe
                                            signo al número, se asume que es positivo.
                                            
                                            * El conjunto de todos los números enteros se representa por la letra ”Z”.
                                            
                                            * En la recta numérica los números negativos se encuentran a la izquierda del cero
                                            y los positivos a su derecha.
                                            
                                            Los números enteros pueden sumarse, restarse, multiplicarse y dividirse,
                                            siguiendo el modelo de los números naturales añadiendo unas normas para el uso
                                            del signo.
                                            
                                            3) ¿Qué se entiende por números racionales?
                                                    
                                            - Son todos los números que pueden representarse como el cociente de dos
                                            números enteros o, más exactamente, un número entero y un número natural; es
                                            decir, una fracción común a/b con numerador a y denominador b distinto de cero. El
                                            conjunto de los números racionales se denota por “Q”. Este conjunto de números
                                            incluye a los números enteros, a los números fraccionarios y es un subconjunto de
                                            los números reales.
                                            
                                            4) ¿Qué son los números irracionales?
                                            - Es cualquier número real que no es racional, y su expresión decimal no es ni
                                            exacta ni periódica.
                                                    
                                            5) ¿Qué se entiende por números reales?
                                            - Son cualquier número que corresponda a un punto en la recta real y pueden
                                            clasificarse en números naturales, enteros, racionales e irracionales. Se denota por
                                            “R”.
                                            
                                            6) ¿Qué se entiende por potencia?
                                            - Es toda base que se repite tantas veces como lo indica un número llamado
                                            exponente.
                                            
                                            Dónde:
                                            
                                            a = Base
                                            
                                            m = exponente
                                                
                                            7) ¿Qué es una cantidad subradical?
                                            
                                            - Es toda aquella que se encuentra dentro de una raíz. Cuando no se vea el índice
                                            de la raíz su valor es 2 (cuadrado).
                                            """)
                                        
                                        elif opcion_matematicas == "2":
                                            print("""
                                            
                                            1) ¿Qué se entiende por polinomio?
                                            - Es una expresión algebraica compuesta por la suma de dos o más términos.
                                            
                                            * Clasificación de los polinomios
                                            
                                            a) Monomios: Solo tienen un solo término.
                                            
                                                P(x) = 1
                                            
                                            b) Binomios: Solo tienen dos términos.
                                            
                                                P(x) = 2x + 1
                                            
                                            c) Trinomios: Solo tienen tres términos.
                                            
                                                P(x) = x elevado a la 2 + 2x + 1
                                            
                                            d) Polinomio propiamente dicho: Poseen más de tres términos.
                                            
                                            * Estructura de un polinomio
                                            Los polinomios se pueden ordenar en forma:
                                            
                                            a) Creciente: Se ordenan los términos de menor a mayor.
                                            
                                            b) Decreciente: Se ordenan los términos de mayor a menor.Grado de un polinomio
                                            
                                            * Es el valor más alto del exponente de la variable polinómica.
                                            * El término independiente del polinomio no va acompañado de la variable
                                            polinómica.
                                            
                                            * Suma y Resta de un polinomio
                    
                                            - Para realizar estas operaciones es necesario que los polinomios estén
                                            ordenados de la misma manera, es decir, en forma decreciente o creciente.
                                            Se recomienda que los polinomios estén ordenados de forma decreciente.
                                            Es conveniente colocar ceros en la posición donde no exista el término
                                            polinomio respectivo, de tal manera de evitar errores en las operaciones.
                                            
                                            * Multiplicación de un polinomio
                                    
                                            Se multiplica cada monomio del primer polinomio por todos los elementos del
                                            segundo polinomio.
                                            
                                            * Se suman los monomios del mismo grado.
                                            
                                            * Se obtiene otro polinomio cuyo grado es la suma de los grados de los
                                            polinomios que se multiplican.
                                            
                                            * División de un polinomio
                                
                                            Que el grado del polinomio dividiendo sea mayor o igual al grado del
                                            polinomio dividir.
                                        
                                            * Si el residuo o polinomio residuo es igual a 0 significa que la división es
                                            exacta.
                                        
                                            * Si el residuo o polinomio residuo es diferente a 0, se observa si el grado de
                                            ese polinomio es mayor o igual al grado del polinomio divisor. Si es así se
                                            realiza nuevamente la división.
                    
                                            * Si el polinomio tiene grado menor al grado del polinomio divisor se deja ahí
                                            la operación.
                                            
                                            Fórmula: D = d · c + R
                                            """)
                                            
                                        
                                        elif opcion_matematicas == "3":
                                            print("""
                                            
                                            1) ¿Qué se entiende por plano cartesiano?
                                            
                                            - Es aquel que está constituido por 2 líneas perpendiculares entre sí. Una línea
                                            horizontal llamada eje de las abscisas (eje X) y una vertical llamada eje de las
                                            ordenadas (eje Y). El punto de intercepción entre ambas líneas se denomina
                                            “origen” o 0 en la escala numérica. Del punto de origen hacia la derecha se
                                            representan los valores positivos y hacia la izquierda los valores negativos en el eje
                                            X; del punto de origen hacia arriba se representan los valores positivos y hacia abajo
                                            los valores negativos en el eje Y.
                                            
                                            El plano real se divide en 4 cuadrantes identificados con números romanos de
                                            derecha a izquierda.
                                            
                                            * Par ordenado o Par cartesiano
                                            Es aquel que determina la ubicación de un punto dentro del plano, utilizando para
                                            ello los valores tanto en el eje X como en el eje Y llamados punto de coordenadas
                                            y su expresión es la siguiente:
                                            
                                            P (X,Y) --------- Identificación del plano.
                                            
                                            2) Líneas de proyección ortogonal
                                            
                                            - Son líneas segmentadas perpendiculares al eje de proyección desde el punto de
                                            ubicación en el plano. Igualmente son líneas paralelas al eje contrario de
                                            proyección.
                                            
                                            2)  Escala numérica en el plano
                                            
                                            - Es la representación numérica en el plano cuyos números dependerá de los
                                            valores de las coordenadas, es decir, si son muy altos se puede establecer una
                                            escala diferente a las de los valores consecutivos. Pueden ser de 2 en 2, 10 en 10,
                                            20 en 20, entre otros.)
                                            
                                            3) Punto en el sistema cartesiano
                                            
                                            * Punto de coordenada: Es aquel punto que permite determinar la ubicación exacta
                                            en el plano o en el espacio (sistema cartesiano).
                                            
                                            4) Rectas paralelas y Rectas perpendiculares
                                            
                                            ¿Qué se entiende por recta paralela?
                                            
                                            - Son aquellas líneas que no se tocan nunca, es decir, son líneas únicas desde el
                                            menos infinito hasta el más infinito.
                                            
                                            ¿Qué se entiende por rectas perpendiculares?
                                                
                                            - Son líneas que se interceptan en un punto formando un ángulo de 90o.
                                            
                                            ¿Qué son líneas secantes?
                                            
                                            - Son líneas que interceptan a otra en un punto formando un ángulo agudo (90o>)
                                            u obtuso (>90o).Dos líneas rectas paralelas son fácilmente identificables ya que su pendiente es
                                            la misma.
                                            
                                            ¿Qué se entiende por pendiente?
                                            
                                            - Es el grado de inclinación de la línea recta.
                                            
                                            * Fórmula para calcular pendiente: m = Y2 – Y1/ X2 – X1
                                            P1 (X1, Y1)
                                            P2 (X2, Y2)
                                            
                                            * Recta punto pendiente
                                            
                                            Si tenemos el valor de un punto perteneciente a una línea y su pendiente,
                                            podemos expresar dicha ecuación como: Y – Y1 = m (X – X1)
                                            
                                            P (X1, Y1)
                                            
                                            * Coordenadas de Baricentro
                                            
                                            Se suman los puntos y se divide entre 3 para el baricentro de un triángulo.
                                            
                                            X = X1 + X2 + X3 / 3
                                            
                                            Y = Y1 + Y2 + Y3 / 3
                                            """)
                                            
                                        
                                        elif opcion_matematicas == "4":
                                            print("""
                                            1) Sistema de ecuaciones

                                            * Ordenar en forma creciente o decreciente las ecuaciones, considerando la
                                            variable por orden alfabético (normalmente).

                                            * Si se ordena la primera ecuación en forma creciente, el resto de las
                                            ecuaciones deben ser ordenadas igual, si fuera decreciente sería del mismo
                                            modo.

                                            * Utilizar cualquier método de resolución para determinar los valores de las
                                            variables que satisfagan la ecuación. Consideraciones para establecer un sistema de ecuaciones
                                            
                                            * Se deben establecer los siguientes criterios para la resolución y aplicación de un
                                            sistema de ecuaciones:

                                            2) Sistemas de ecuaciones compatibles: 
                                            - Son aquellas que admiten solución, se clasifican en:

                                            a) Compatibles determinadas: Son aquellas que admiten una única solución.

                                            b) Compatibles indeterminadas: Son aquellas que admiten muchas soluciones.

                                            3) Sistemas de ecuaciones incompatibles: 
                                            
                                            - Son aquellas que no admiten ninguna solución.
                                            
                                            a) Método de Eliminación
                                            - Este método consiste en buscar eliminar una primera variable con el propósito
                                            de encontrar la o las siguientes.
                                            Si fuese necesario, habrá que utilizar un factor multiplicador para poder igualar
                                            el término en la cual se encuentra la variable a eliminar.

                                            3) Sistema de ecuación con 3 incógnitas
                                                
                                            - Es el sistema que permite introducir una nueva variable que determina la
                                            compatibilidad o incompatibilidad del sistema.Proceso de solución

                                            a) Se toma la ecuación 1 y 2, y se elimina alguna de las incógnitas.

                                            b) Se forma la primera ecuación con 2 incógnitas.

                                            c) Se combina la ecuación 1 con la 3 y se obtiene la segunda ecuación
                                            semejante a la primera.

                                            d) A partir del sistema de ecuaciones con 2 incógnitas, se calculan ambas
                                            incógnitas siguiendo el método ya estudiado.

                                            e) Una vez obtenido el valor de las incógnitas, se procede a seleccionar del
                                            sistema original de 3 incógnitas, una de las ecuaciones y se sustituye las
                                            variables cuyo valor fue encontrado para obtener la tercera incógnita a través
                                            de las operaciones básicas elementales.
                                            """)
                                                        
                    elif opcion_glosario == "3":
                        break      
                            
        elif eleccion == 15:
                
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
                      8- Volver al menú principal
                      
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
                    break
            
        elif eleccion == 16:
            
            print("*" * 80)
            print("")
            print("Programa creado por los estudiantes Siugel Chong y Luis Diego Salas")
            print("")
            print("Ruben Leal como nuestro asesor")
            print("")
            print("Unidad Psicoeducativa Julio Chevalier")
            print("")
            print("Reto de matemáticas 2024")
            print("")
            print("*" * 80)

import streamlit as st
import pandas as pd
import math
from pathlib import Path

def saludar():
    st.write("¡Hola! Bienvenido al programa.")
    
def suma(a,b):
    return a+b

def area_triangulo(base, altura):
    area=base*altura/2
    return area

def calcular_precio_final(p_original,porc_impuesto,porc_descuento):
    descuento=(porc_descuento/100)*p_original
    p_descuento=p_original-descuento
    impuesto=(porc_impuesto/100)*p_descuento
    p_final=p_descuento-impuesto
    return p_final

def sumar_lista(lista):
    suma = 0
    for numero in lista:
        suma += numero
    return suma

# Función para ingresar la lista de números
def ingresar_lista(opcion):
    entrada = input("Ingrese los números separados por comas: ")
    # Convertir la entrada en una lista de números
    lista_numeros = [float(num) for num in entrada.split(",")]
    
    if opcion == 'suma':
        resultado = sumar_lista(lista_numeros)
        print(f"La suma de los números ingresados es: {resultado}")
    elif opcion == 'pares_impares':
        pares, impares = numeros_pares_e_impares(lista_numeros)
        print(f"Números pares: {pares}")
        print(f"Números impares: {impares}")

def producto(nombre, cantidad=1, precio=10):
    total = cantidad * precio
    return f"El total a pagar por {cantidad} {nombre}/S es: {total} Pesos."

def ingresar_datosproducto():
    nombre = input("Ingrese el nombre del producto: ")
    cantidad = int(input("Ingrese la cantidad: "))
    precio = float(input("Ingrese el precio por unidad: "))
    
    resultado = producto(nombre, cantidad, precio)
    print(resultado)

def numeros_pares_e_impares(lista):
    pares = []
    impares = []
    
    for numero in lista:
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)
    
    return pares, impares

def multiplicar_todos(*args):
    resultado = 1
    for numero in args:
        resultado *= numero
    return resultado

def solicitar_numeros():
    st.title("Multiplicación de Números")
    numeros = []
    
    entrada = st.text_input("Ingresa números separados por comas (ej. 1, 2, 3):")
    
    if entrada:
        try:
            # Convertimos la entrada a una lista de números
            numeros = list(map(float, entrada.split(',')))
            resultado = multiplicar_todos(*numeros)
            st.write(f"\nEl resultado de multiplicar todos los números es: {resultado}")
        except ValueError:
            st.write("Entrada no válida, por favor ingresa solo números.")

def informacion_personal(**kwargs):
    st.write("\nInformación personal ingresada:")
    for clave, valor in kwargs.items():
        st.write(f'{clave}: {valor}')

def menu_informacion_personal():
    st.title("Menú de Información Personal")
    
    # Crear un diccionario para almacenar la información proporcionada
    informacion = {}
    
    nombre = st.text_input("Ingresa tu nombre:")
    if nombre:
        informacion['Nombre'] = nombre
        
    edad = st.number_input("Ingresa tu edad:", min_value=0)
    if edad:
        informacion['Edad'] = edad
        
    direccion = st.text_input("Ingresa tu dirección:")
    if direccion:
        informacion['Dirección'] = direccion
        
    telefono = st.text_input("Ingresa tu teléfono:")
    if telefono:
        informacion['Teléfono'] = telefono
        
    if st.button("Mostrar información"):
        # Llamar a la función para mostrar la información proporcionada
        informacion_personal(**informacion)


def calculadora_flexible(num1, num2, operacion="suma"):
    if operacion == "suma":
        return num1 + num2
    elif operacion == "resta":
        return num1 - num2
    elif operacion == "multiplicacion":
        return num1 * num2
    elif operacion == "division":
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: División por cero"
    else:
        return "Operación no válida"

def menu_calculadora():
    st.title("Calculadora Flexible")
    
    # Ingreso de números
    num1 = st.number_input("Ingresa el primer número:", format="%.2f")
    num2 = st.number_input("Ingresa el segundo número:", format="%.2f")
    
    # Selección de operación
    operacion = st.selectbox("Selecciona la operación:", ["suma", "resta", "multiplicacion", "division"])
    
    # Botón para calcular
    if st.button("Calcular"):
        resultado = calculadora_flexible(num1, num2, operacion)
        st.write(f"\nEl resultado de la {operacion} es: {resultado}")


# Configuración de la página
st.title("Menú Principal")

# Interfaz del menú
opcion = st.selectbox("Elige una opción:", [
    "Saludo",
    "Sumar dos números",
    "Calcular área de un triángulo",
    "Calcular precio final",
    "Sumar una lista de números",
    "Calcular producto de una lista de números",
    "Separar números pares e impares",
    "Multiplicar números de una lista",
    "Ingresar información personal",
    "Calculadora flexible",
    "Salir"
])

# Ejecutar función basada en la opción elegida
if opcion == "Saludo":
    saludar()

elif opcion == "Sumar dos números":
    a = st.number_input("Ingresa el primer número:", format="%.2f")
    b = st.number_input("Ingresa el segundo número:", format="%.2f")
    if st.button("Calcular suma"):
        resultado = suma(a, b)
        st.write(f"La suma de {a} y {b} es: {resultado}")

elif opcion == "Calcular área de un triángulo":
    base = st.number_input("Ingresa la base del triángulo:", format="%.2f")
    altura = st.number_input("Ingresa la altura del triángulo:", format="%.2f")
    if st.button("Calcular área"):
        area = area_triangulo(base, altura)
        st.write(f"El área del triángulo es: {area}")

elif opcion == "Calcular precio final":
    p_original = st.number_input("Ingresa el precio original:", format="%.2f")
    porc_impuesto = st.number_input("Ingresa el porcentaje de impuesto:", format="%.2f")
    porc_descuento = st.number_input("Ingresa el porcentaje de descuento:", format="%.2f")
    if st.button("Calcular precio final"):
        precio_final = calcular_precio_final(p_original, porc_impuesto, porc_descuento)
        st.write(f"El precio final es: {precio_final}")

elif opcion == "Sumar una lista de números":
    ingresar_lista()

elif opcion == "Calcular producto de una lista de números":
    solicitar_numeros()

elif opcion == "Ingresar información personal":
    menu_informacion_personal()

elif opcion == "Calculadora flexible":
    menu_calculadora()

elif opcion == "Salir":
    st.write("Saliendo del programa.")

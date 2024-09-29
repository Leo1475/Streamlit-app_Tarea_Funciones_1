import streamlit as st

#Saludar
def saludar(nombre):
    return f"Hola, {nombre}"

#Sumar dos números
def sumar(a, b):
    return a + b

#Área de un triángulo
def calcular_area_triangulo(base, altura):
    return (base * altura) / 2

#Calculadora de descuento
def calcular_precio_final(precio, descuento=10, impuesto=16):
    precio_descuento = precio - (precio * descuento / 100)
    precio_final = precio_descuento + (precio_descuento * impuesto / 100)
    return precio_final

#Sumar lista de números
def sumar_lista(numeros):
    return sum(numeros)

#Producto con valores predeterminados
def producto(nombre, cantidad=1, precio_por_unidad=10):
    return cantidad * precio_por_unidad

#Números pares e impares
def numeros_pares_e_impares(lista):
    pares = [x for x in lista if x % 2 == 0]
    impares = [x for x in lista if x % 2 != 0]
    return pares, impares

#Multiplicación con *args
def multiplicar_todos(*args):
    resultado = 1
    for num in args:
        resultado *= num
    return resultado

#Información personal con **kwargs
def informacion_personal(**kwargs):
    info = "\n".join([f"{k}: {v}" for k, v in kwargs.items()])
    return info

#Calculadora flexible
def calculadora_flexible(a, b, operacion='suma'):
    if operacion == 'suma':
        return a + b
    elif operacion == 'resta':
        return a - b
    elif operacion == 'multiplicacion':
        return a * b
    elif operacion == 'division':
        return a / b if b != 0 else "No se puede dividir entre 0"
    else:
        return "Operación no válida"

#Aplicación en Streamlit

st.title("Tablero Interactivo de Funciones en Python")

#Selección el ejercicio
opcion = st.sidebar.selectbox(
    "Selecciona un ejercicio",
    ("Saludar", "Sumar dos números", "Área de un triángulo", 
     "Calculadora de descuento", "Sumar lista de números",
     "Producto con valores predeterminados", "Números pares e impares", 
     "Multiplicación con *args", "Información personal con **kwargs", 
     "Calculadora flexible")
)

#Saludar
if opcion == "Saludar":
    nombre = st.text_input("Ingresa tu nombre")
    if st.button("Saludar"):
        st.write(saludar(nombre))

#Sumar dos números
elif opcion == "Sumar dos números":
    a = st.number_input("Número 1", value=0)
    b = st.number_input("Número 2", value=0)
    if st.button("Sumar"):
        st.write(f"La suma es: {sumar(a, b)}")

#Área de un triángulo
elif opcion == "Área de un triángulo":
    base = st.number_input("Base", value=0.0)
    altura = st.number_input("Altura", value=0.0)
    if st.button("Calcular área"):
        st.write(f"El área del triángulo es: {calcular_area_triangulo(base, altura)}")

#Calculadora de descuento
elif opcion == "Calculadora de descuento":
    precio = st.number_input("Precio original", value=0.0)
    descuento = st.number_input("Descuento (%)", value=10.0)
    impuesto = st.number_input("Impuesto (%)", value=16.0)
    if st.button("Calcular precio final"):
        st.write(f"El precio final es: {calcular_precio_final(precio, descuento, impuesto)}")

#Sumar lista de números
elif opcion == "Sumar lista de números":
    lista_numeros = st.text_area("Ingresa una lista de números separados por comas")
    if st.button("Sumar lista"):
        lista = [float(x) for x in lista_numeros.split(",")]
        st.write(f"La suma de la lista es: {sumar_lista(lista)}")

#Producto con valores predeterminados
elif opcion == "Producto con valores predeterminados":
    nombre_producto = st.text_input("Nombre del producto")
    cantidad = st.number_input("Cantidad", value=1)
    precio_unidad = st.number_input("Precio por unidad", value=10.0)
    if st.button("Calcular total"):
        st.write(f"El total es: {producto(nombre_producto, cantidad, precio_unidad)}")

#Números pares e impares
elif opcion == "Números pares e impares":
    lista_numeros = st.text_area("Ingresa una lista de números separados por comas")
    if st.button("Separar pares e impares"):
        lista = [int(x) for x in lista_numeros.split(",")]
        pares, impares = numeros_pares_e_impares(lista)
        st.write(f"Números pares: {pares}")
        st.write(f"Números impares: {impares}")

#Multiplicación con *args
elif opcion == "Multiplicación con *args":
    lista_numeros = st.text_area("Ingresa los números separados por comas")
    if st.button("Multiplicar todos"):
        lista = [float(x) for x in lista_numeros.split(",")]
        st.write(f"El resultado de la multiplicación es: {multiplicar_todos(*lista)}")

#Información personal con **kwargs
elif opcion == "Información personal con **kwargs":
    nombre = st.text_input("Nombre")
    edad = st.number_input("Edad", value=0)
    direccion = st.text_input("Dirección")
    if st.button("Mostrar información"):
        st.write(informacion_personal(nombre=nombre, edad=edad, direccion=direccion))

#Calculadora flexible
elif opcion == "Calculadora flexible":
    a = st.number_input("Número 1", value=0.0)
    b = st.number_input("Número 2", value=0.0)
    operacion = st.selectbox("Operación", ["suma", "resta", "multiplicacion", "division"])
    if st.button("Calcular"):
        st.write(f"El resultado es: {calculadora_flexible(a, b, operacion)}")

#Comando de ejecución:  Streamlit run Tarea_Funciones_1.py
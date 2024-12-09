#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Conversor de temperaturas | Pablo P.H.

#Función que convierte temperaturas entre diferentes unidades
def convertir_temperatura(valor, unidad_origen, unidad_destino):
    if unidad_origen == "C":
        if unidad_destino == "F":
            return (valor * 9/5) + 32
        elif unidad_destino == "K":
            return valor + 273.15
    elif unidad_origen == "F":
        if unidad_destino == "C":
            return (valor - 32) * 5/9
        elif unidad_destino == "K":
            return (valor - 32) * 5/9 + 273.15
    elif unidad_origen == "K":
        if unidad_destino == "C":
            return valor - 273.15
        elif unidad_destino == "F":
            return (valor - 273.15) * 9/5 + 32
    else:
        raise ValueError("Unidad no válida. Usa 'C', 'F' o 'K'.")
        

#Comprobamos que introduzca el valor como corresponde
def comprobar_numeros(valor):
    contador = 0
    punto_encontrado = False
    numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for caracter in valor:
        if caracter == '-' and contador != 0:
            print('Error: Ha introducido un "-" cuando no corresponde')
            return False
        if caracter == '.':
            if punto_encontrado:
                print('Error: Ha introducido más de un punto')
            punto_encontrado = True
        elif caracter not in numeros:
            print("Error: Debe introducir solo números en el valor de la temperatura")
            return False
        contador += 1
    return True

#Función principal que interactúa con el usuario
def main():
    print("Bienvenido al convertidor de temperaturas")
    print("Este programa convierte temperaturas entre Celsius, Fahrenheit y Kelvin.")
    #Separador visual
    print("-" * 40)
    
    valor = input("Introduce el valor de la temperatura: ").strip()
    #Comprobamos que el valor introducido es correcto
    while comprobar_numeros (valor) == False:
        print('Vuelva a introducir los valores')
        valor = input("Vuelva a introducir un valor válido: ").strip()        
    valor = float(valor)
    
    #Comprobamos que ha introducido bien la unidad origen y destino 
    while True:
        unidad_origen = input("Introduce la unidad de origen ('C', 'F', 'K'): ").upper().strip()
        if unidad_origen not in ['C', 'F', 'K']:
            print("Unidad de origen no válida. Debe ser 'C', 'F' o 'K'.")
        else:
            break

    while True:
        unidad_destino = input("Introduce la unidad de destino ('C', 'F', 'K'): ").upper().strip()
        if unidad_destino not in ['C', 'F', 'K']:
            print("Unidad de destino no válida. Debe ser 'C', 'F' o 'K'.")
        else:
            break
        
    try:
        #Llamar a la función de conversión y mostrar el resultado
        resultado = convertir_temperatura(valor, unidad_origen, unidad_destino)
        print(f"{valor} {unidad_origen} es igual a {resultado} {unidad_destino}")
    except ValueError as e:
        print(f"Error: {e}")

#Ejecutar main solo si el script es ejecutado directamente
if __name__ == "__main__":
    main()


# In[5]:





# In[ ]:





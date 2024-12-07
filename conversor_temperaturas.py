#!/usr/bin/env python
# coding: utf-8

# In[1]:


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

#Función principal que interactúa con el usuario
def main():
    print("Bienvenido al convertidor de temperaturas")
    valor = float(input("Introduce el valor de la temperatura: "))
    unidad_origen = input("Introduce la unidad de origen ('C', 'F', 'K'): ").upper()
    unidad_destino = input("Introduce la unidad de destino ('C', 'F', 'K'): ").upper()

    try:
        #Llamar a la función de conversión y mostrar el resultado
        resultado = convertir_temperatura(valor, unidad_origen, unidad_destino)
        print(f"{valor} {unidad_origen} es igual a {resultado} {unidad_destino}")
    except ValueError as e:
        print(f"Error: {e}")

#Ejecutar main solo si el script es ejecutado directamente
if __name__ == "__main__":
    main()


# In[ ]:





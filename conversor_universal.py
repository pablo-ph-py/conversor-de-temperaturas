#!/usr/bin/env python
# coding: utf-8

# Conversor Universal | Pablo P.H.

import requests


# Conversor de Temperaturas
def convertir_temperatura(valor, unidad_origen, unidad_destino):
    if unidad_origen == "C":
        if unidad_destino == "F":
            return (valor * 9 / 5) + 32
        elif unidad_destino == "K":
            return valor + 273.15
    elif unidad_origen == "F":
        if unidad_destino == "C":
            return (valor - 32) * 5 / 9
        elif unidad_destino == "K":
            return (valor - 32) * 5 / 9 + 273.15
    elif unidad_origen == "K":
        if unidad_destino == "C":
            return valor - 273.15
        elif unidad_destino == "F":
            return (valor - 273.15) * 9 / 5 + 32
    else:
        raise ValueError("Unidad no válida. Usa 'C', 'F' o 'K'.")


def comprobar_numeros(valor):
    try:
        float(valor)
        return True
    except ValueError:
        return False


# Conversor de Monedas
MONEDAS_ACEPTADAS = ["USD", "EUR", "JPY", "GBP", "AUD", "CAD", "CHF", "CNY", "SEK", "NZD"]


def validar_moneda(moneda):
    return moneda in MONEDAS_ACEPTADAS


def obtener_tasa_cambio(moneda_origen, moneda_destino):
    if not validar_moneda(moneda_origen) or not validar_moneda(moneda_destino):
        print(f"Error: Moneda no válida. Monedas aceptadas: {', '.join(MONEDAS_ACEPTADAS)}")
        return None

    API_URL = f"https://v6.exchangerate-api.com/v6/52ebb3bb9d4d1aa363391b50/pair/{moneda_origen}/{moneda_destino}"
    try:
        respuesta = requests.get(API_URL)
        respuesta.raise_for_status()
        datos = respuesta.json()

        if datos["result"] == "success":
            return datos["conversion_rate"]
        else:
            print(f"Error en la API: {datos.get('error-type', 'Error desconocido')}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error al conectar con la API: {e}")
        return None


def convertir_moneda(cantidad, moneda_origen, moneda_destino):
    tasa = obtener_tasa_cambio(moneda_origen, moneda_destino)
    if tasa is None:
        return None
    return cantidad * tasa


# Función principal
def main():
    print("Bienvenido al convertidor de Temperaturas y Monedas")
    print("Este programa convierte temperaturas y monedas en tiempo real.")
    print("-" * 40)

    while True:
        print("\nMenú:")
        print("1. Conversor de Temperatura")
        print("2. Conversor de Moneda")
        print("3. Salir")
        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            valor = input("Introduce el valor de la temperatura: ").strip()
            while not comprobar_numeros(valor):
                print("Error: Debe introducir solo números en el valor de la temperatura")
                valor = input("Vuelva a introducir un valor válido: ").strip()
            valor = float(valor)

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
                resultado = convertir_temperatura(valor, unidad_origen, unidad_destino)
                print(f"{valor} {unidad_origen} es igual a {resultado} {unidad_destino}")
            except ValueError as e:
                print(f"Error: {e}")

        elif opcion == "2":
            cantidad = input("Introduce la cantidad de dinero: ").strip()
            while not comprobar_numeros(cantidad):
                print("Error: Debe introducir un número válido.")
                cantidad = input("Introduce una cantidad válida: ").strip()
            cantidad = float(cantidad)

            moneda_origen = input(f"Introduce la moneda de origen (Ej.: {', '.join(MONEDAS_ACEPTADAS)}): ").upper().strip()
            while not validar_moneda(moneda_origen):
                print(f"Moneda de origen no válida. Monedas aceptadas: {', '.join(MONEDAS_ACEPTADAS)}")
                moneda_origen = input("Introduce una moneda válida: ").upper().strip()

            moneda_destino = input(f"Introduce la moneda de destino (Ej.: {', '.join(MONEDAS_ACEPTADAS)}): ").upper().strip()
            while not validar_moneda(moneda_destino):
                print(f"Moneda de destino no válida. Monedas aceptadas: {', '.join(MONEDAS_ACEPTADAS)}")
                moneda_destino = input("Introduce una moneda válida: ").upper().strip()

            resultado = convertir_moneda(cantidad, moneda_origen, moneda_destino)
            if resultado is not None:
                print(f"{cantidad:.2f} {moneda_origen} es igual a {resultado:.2f} {moneda_destino}")
            else:
                print("No se pudo realizar la conversión. Revisa las monedas introducidas.")

        elif opcion == "3":
            print("Gracias por usar el convertidor. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")


if __name__ == "__main__":
    main()

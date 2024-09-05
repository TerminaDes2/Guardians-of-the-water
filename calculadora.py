def convertir_base(numero, base_origen, base_destino):
    # Convertir el número de la base de origen a base 10
    numero_base10 = int(numero, base_origen)
    
    # Convertir el número de base 10 a la base de destino
    if base_destino == 10:
        return str(numero_base10)
    
    digitos = "0123456789ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    resultado = ""
    while numero_base10 > 0:
        resultado = digitos[numero_base10 % base_destino] + resultado
        numero_base10 //= base_destino
    
    return resultado

# Ejemplo de uso
numero = input("Introduce el número a convertir: ")
base_origen = int(input("Introduce la base de origen (2-36): "))
base_destino = int(input("Introduce la base de destino (2-36): "))

resultado = convertir_base(numero, base_origen, base_destino)
print(f"El número {numero} en base {base_origen} es {resultado} en base {base_destino}.")

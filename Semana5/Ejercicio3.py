'''Cajero automático: validación de retiro
Un cajero permite retirar solo montos mayores a 0 y múltiplos de 10.
Solicita el monto hasta que sea válido y luego muestra "Retiro exitoso".'''


print("CAJERO AUTOMATICO")

monto_retirar = int(input("ingresa un monto a retirar, solo multiplos de 10 (presiona 0 para salir): "))
while monto_retirar != 0:
    print("ingresaste",monto_retirar,)
    if monto_retirar % 10 == 0:
        print("monto a retirar exitoso")
    else:
        print("monto invalido")
    monto_retirar = int(input("ingresa un monto a retirar(presiona 0 para salir): "))
print("adios :D ")



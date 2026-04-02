'''Control de temperatura
Un sistema de climatización clasifica:
"Fría": menos de 10°C
"Templada": entre 10 y 25
"Calurosa": más de 25
Solicita la temperatura e indica la clasificación correspondiente.
'''

print("bienvenido")
clima = int(input("cuantos grados hay actualmente: "))

if clima < 10:
    print("es una temperatura fria")
elif clima >= 10 or clima <=25:
    print("es una temperatura templada")
elif clima > 25:
    print("es una temperatura calurosa")






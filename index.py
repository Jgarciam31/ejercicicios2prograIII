import os
import msvcrt
from Impar import impar
from Par import par
op=0

#MENU
while True:
    print("------------------------------------------------------------------------------------------------------------------")
    print("                                                   EJERCICIOS 2")
    print("------------------------------------------------------------------------------------------------------------------")
    print("1. Leer un numero y mostrar su tabla de multiplicar")
    print("2. Leer una secuencia de 30 numeros y mostrar la suma y el producto de ellos")
    print("3. Leer una secuencia de numeros hasta que se intruduzca uno negativo y mostrar la suma")
    print("4. Leer dos numeros y realizar el producto mediante sumas")
    print("5. Leer dos unmero y realizar la division mediante restas mostrando el cociente y el resto")
    print("6. Leer una secuencia de numeros y mostrar su producto, el proceso finalizara cuando el usuario puse la letra F")
    print("7. Leer una secuencia de numeros y determinar cual es el mayor de ellos")
    print("8. Dado un numero mostrar cual es el valor en binario")
    print("9. Generar enteros de 3 en 3 comenzando por 2 hasta el valor máximo menor que calculando la suma de los enteros generados que sean divisibles por 5.")
    print("10.Calcular la media de una secuencia de números, el proceso finalizará cuando el usuario pulse F.  ")
    print("11.Generar los N primeros términos de la serie de Fibonacci y mostrarlos por pantalla")
    print("12. Leer una secuencia se números y mostrar cuáles de ellos es el mayor y el menor, el proceso finalizará cuando se introduzca un número impar.   " )
    print("13. Leer una secuencia de números y sumar solo los pares mostrando el resultado del proceso.   ")
    print("14. Leer una secuencia de números y mostrar la suma de los 30 números que ocupan posiciones de lectura par.   ")
    print("15. Leer un número y determinar su factorial. ")
    print("------------------------------------------------------------------------------------------------------------------")
    op = int(input("Ingresar Opcion: "))

    if op == 1:
        print("Leer un numero y mostrar su tabla de multiplicar")
        print(impar.uno())

    elif op == 2:
        print("Leer una secuencia de 30 numeros y mostrar la suma y el producto de ellos")
        print(par.dos())

    elif op == 3:
        print("Leer una secuencia de numeros hasta que se intruduzca uno negativo y mostrar la suma")
        print(impar.tres())

    elif op == 4:
        print("Leer dos numeros y realizar el producto mediante sumas")
        print(par.cuatro())

    elif op == 5:
        print("Leer dos unmero y realizar la division mediante restas mostrando el cociente y el resto")
        print(impar.cinco())

    elif op == 6:
        print("Leer una secuencia de numeros y mostrar su producto, el proceso finalizara cuando el usuario puse la letra F")
        print(par.seis())

    elif op == 7:
        print("Leer una secuencia de numeros y determinar cual es el mayor de ellos")
        print(impar.siete())

    elif op == 8:
        print("Dado un numero mostrar cual es el valor en binario")
        print(par.ocho())


    elif op == 9:
        print("Generar enteros de 3 en 3 comenzando por 2 hasta el valor máximo menor que calculando la suma de los enteros generados que sean divisibles por 5.")
        print("No Pude realizar esta opcion inge perdon :'c")


    elif op == 10:
        print("Calcular la media de una secuencia de números, el proceso finalizará cuando el usuario pulse F. ")
        print(par.diez())

    elif op == 11:

        print(impar.once())
        print("11. Generar los N primeros términos de la serie de Fibonacci y mostrarlos por pantalla")
        print("Para repetir el menu...")
        break
    elif op == 12:
        print("No Pude realizar esta opcion inge perdon :'c")

    elif op == 13:
        print("No Pude realizar esta opcion inge perdon :'c")

    elif op == 14:
        print("No Pude realizar esta opcion inge perdon :'c")

    elif op == 15:
        print("15. Leer un número y determinar su factorial.")
        print(impar.quince())

    input()
    os.system("cls")

print("Finaliza el Programa")

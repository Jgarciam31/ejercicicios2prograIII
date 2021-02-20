import msvcrt


class par():

    def dos():
        lista = []
        cantidad = 30
        suma = 0
        prod = 1

        while (cantidad > 0):
            numero = int(input("Dijite el numero: "))
            lista.append(numero)
            cantidad = cantidad - 1

        for i in lista:
            suma = suma + i

        for i in lista:
            prod = prod * i

        print(f"La suma de los numeros es: {suma}")
        print(f"El producto de los numeros es: {prod}")


    def cuatro():
        primerNumero = int(input("Dijite Primer Numero: "))
        segudnoNumero = int(input("Dijite Segudno Numero: "))
        n = primerNumero + 1
        resultado = 0
        for i in range(1, n):
            resultado = resultado + segudnoNumero
            print(resultado)

        print(f"El resultado es:  {resultado}")


    def seis():
        salir = ""
        resultado = 1
        while (salir != "f"):
            salir = str(input("Dijite Un Numero: "))
            if (salir != "f"):
                print(f"El resultado es:  {salir}")
                resultado = resultado * int(salir)
                print(resultado)
            else:
                print("Usted ha salido del programa")


    def ocho():
        primerNumero = (int(input("Ingrese numero: ")))
        numero = bin(primerNumero)
        print(f"el numero binario es: {numero}")

    def diez():
        suma=0
        contador=0
        numero=0
        F = 0

        while True:
            numero = int(input("Ingrese un numero: "))
            if msvcrt.kbhit() and msvcrt.getwch() == 'F':
                break
        suma += numero
        contador += 1
        if contador == 0:
            print("No ingreso ningun numero")
        else:
            promedio = suma / contador
            print("El promedio de los {} numeros es igual a {} ".format(contador, promedio))
            print("Presione Enter para mostrar el menu")

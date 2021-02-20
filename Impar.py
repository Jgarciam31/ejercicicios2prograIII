import msvcrt
class impar():


    def uno():
        n = int(input("Dijite Numero: "))
        for i in range(11):
            mul = n * i
            print(n, " * ", i, " = ", mul)

    def tres():
        numero = 1
        resultado = 0
        while (numero > 0):
            numero = int(input("Dijite Un Numero: "))
            if (numero > 0):
                print(f"El resultado es:  {numero}")
                resultado = resultado + numero
                print(resultado)
            else:
                print("Usted ha salido del programa")


    def cinco():
        contador = int(0)
        dividendo = int(input("Dijite el dividendo: "))
        divisor = int(input("Dijite el divisor: "))

        dividendo = dividendo - divisor
        while (dividendo >= 0):
            contador = contador + 1
            dividendo = dividendo - divisor
        print(f"El resultado es:  {contador}")


    def siete():
        lista = []
        cantidad = int(input("Dijite cuantos numeros desea ingresar: "))
        mayor = 0

        while (cantidad > 0):
            numero = int(input("Dijite un Numero: "))
            lista.append(numero)
            cantidad = cantidad - 1

        mayor = max(lista)
        print(f"El numero mayor es: {mayor}")

    def once():
        i = 0
        num = 0
        numero1 = 0
        numero2 = 1
        numero3 = 0

        while True:
            num = int(input("Ingrese un numero mayor a 1: "))
            if num > 1:
                break
        print("1", end=" ")
        for n in range(0, i.num):
            numero3 = numero1 + numero2
            print(f"{numero3}", end=" ")
            numero1 = numero2
            numero2 = numero3
        print("")
        print("Presione Enter para mostrar el menu")


    def quince():
        contador = 0
        factorial = 1
        n = 0
        contador = int(input("Ingrese un numero: "))
        for n in range(contador):
            print(factorial, "*", contador)
            factorial *= contador
            contador -= 1
            print(f"Resultado: %d", factorial)

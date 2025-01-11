print("Hola mundo")
nombre=input("Dime tu nombre: ")
print("Hola,",nombre)
MayorDeEdad=18
edad=int(input("Ingrese su edad: "))
resultado=edad>=MayorDeEdad
print("¿Es mayor de edad?", resultado)
número=int(input("Ingrese un número: "))
if número % 2 == 0:
    print("Su número es par")
else:
    print ("Su número es impar")
número_entero=int(input("Ingrese un número entero: "))
número1=1
número2=2
suma=int(número_entero*(número_entero+número1)/número2)
print("El resultado es", suma)
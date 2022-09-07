# ciclo mientras 



# la ejecución de mi ciclo
#i = 0


# #programar la estructura del ciclo mientras
# while(i < 20):
#     print("Estoy saltando cuerda",i)
#     i = i + 1 #contador
# print("Terminamos de saltar")


# #programar la estructura del ciclo mientras caso con input
# while(i >= 0):
#     i = int(input("Digite un número: "))
#     print("Estoy saltando cuerda",i)
# print("Terminamos de saltar")

# i=0
# #programar la estructura del ciclo mientras excluiyendo
# while(i!=5):
#     i = int(input("Digite un número: "))
#     print("Estoy saltando cuerda",i)
# print("Terminamos de saltar")

# i=0
# # menu
# print("***MENU***")
# print("1. Saludar")
# print("2. Despedir")
# print("3. quien gano")
# print("4. contar si esta lloviendo")
# print("5. Salir")

# #programar la estructura del ciclo mientras menu de opciones
# while(i!=5):
#     i = int(input("Digite la opción del menú: "))
#     if(i==1):
#         print("Hola cómo estás? ")
#     elif(i==2):
#         print("Chao amor")
#     elif(i==3):
#         print("Ganador el rojo")
#     elif(i==4):
#         print("No llueve en Medellin")
#     elif(i==5):
#         Break
#     else:
#         print("Digite una opción correcta")

# print("Salimos del while")





import math


i=0
num1 = 0
num2 = 0
suma =0
resta = 0
mult = 0
raiz = 0

# menu
print("***MENU***")
print("1. Sumar 2 números")
print("2. Restar 2 números")
print("3. Encontrar la raiz cuadrada de un número")
print("4. Restar 2 números")
print("5. Salir")

#programar la estructura del ciclo mientras menu de opciones
while(i!=5):
    i = int(input("Digite la opción del menú: "))
    if(i==1):
        num1 = int(input("Digite el primer número"))
        num2 = int(input("Digite el primer número"))
        sum =  num1 + num2
        print("El resultados es ", sum)

    elif(i==2):
        num1 = int(input("Digite el primer número"))
        num2 = int(input("Digite el primer número"))
        resta =  num1 - num2
        print("El resultados es ", resta)

    elif(i==3):
        num1 = int(input("Digite el primer número"))
        num2 = int(input("Digite el primer número"))
        mult =  num1 * num2
        print("El resultados es ", mult)
    elif(i==4):
        num1 = int(input("Digite el  número"))
        raiz =  math.sqrt(num1)
        print("El resultados es ", raiz)
        
    elif(i==5):
        break
    else:
        print("Digite una opción correcta")

print("Salimos del while")

controladora = 100

print("Empanadas machetico")
print("********************")
print("1. Agregar sabor de empanada")
print("2. Mostrar sabores de empanada")
print("3. Editar sabor de empanada")
print("4. SALIR")

while (controladora != 0):
    empanada = None
    controladora = int(input("Digita una opción: "))
    if (controladora == 1):
        empanada = input("Digita el sabor de la empanada: ")
    elif controladora == 2:
        empanada = input("El sabor es: {empanada}")
    elif controladora == 3:
        empanada = input("Digita el nuevo sabor de la empanada: ")
    elif controladora == 0:
        print("Saliendo del programa")
        break
    else:
        print("Opción no valida")


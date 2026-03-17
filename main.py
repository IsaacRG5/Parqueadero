TOTAL_ESPACIOS = 10
parqueadero = ["ABC123", "DEF456", "GHI789", "JKL321", "MNO654",
            "Libre", "Libre", "Libre", "Libre", "Libre"]

vacio = True

try:
    while vacio:
        print("\n===== PARQUEADERO =====")
        print("1. Mostrar estado")
        print("2. Ingresar vehículo")
        print("3. Retirar vehículo")
        print("4. Salir")

        opcion = int(input("Escoja la opcion: "))

        if opcion == 1:
            print("\n--- ESTADO DEL PARQUEADERO ---")
            
            with open("parqueadero.txt", "r") as park:
                
                for i, matricula in enumerate(park): 
                    print("Espacio", i + 1, ":", matricula)

        elif opcion == 2:
            placa = input("Ingrese la placa: ")

            if "Libre" in parqueadero:
                posicion = parqueadero.index("Libre")
                parqueadero[posicion] = placa
                print("Vehículo ingresado en el espacio", posicion + 1)

                archivo = open("parqueadero.txt", "w")
                for i in range(TOTAL_ESPACIOS):
                    archivo.write(parqueadero[i] + "\n")
                archivo.close()

            else:
                print("Parqueadero lleno")

        elif opcion == 3:
            placa = input("Ingrese la placa a retirar: ")

            if placa in parqueadero:
                posicion = parqueadero.index(placa)
                parqueadero[posicion] = "Libre"
                print("Vehículo retirado del espacio", posicion + 1)

                archivo = open("parqueadero.txt", "w")
                for i in range(TOTAL_ESPACIOS):
                    archivo.write(parqueadero[i] + "\n")
                archivo.close()

            else:
                print("Placa no encontrada")

        elif opcion == 4:
            print("Sistema finalizado")
            break

        else:
            print("Opción inválida")

except ValueError:
    print("ERROR")
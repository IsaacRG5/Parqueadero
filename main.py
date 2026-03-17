TOTAl_ESPACIOS = 10
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
                for i in range(TOTAl_ESPACIOS):
                    print("Espacio", i + 1, ":", parqueadero[i])

        elif opcion == 2:
                placa = input("Ingrese la placa: ")
                
                if "Libre" in parqueadero:
                    posicion = parqueadero.index("Libre")
                    parqueadero[posicion] = placa
                    print("Vehículo ingresado en el espacio", posicion + 1)
                else:
                    print("Parqueadero lleno")

        elif opcion == 3:
                placa = input("Ingrese la placa a retirar: ")
                
                if placa in parqueadero:
                    posicion = parqueadero.index(placa)
                    parqueadero[posicion] = "Libre"
                    print("Vehículo retirado del espacio", posicion + 1)
                else:
                    print("Placa no encontrada")
        elif opcion == "4":
                    print("Sistema finalizado")

                    with open("Registro_parqueadero.txt", "w") as archivo:
                        for placa in parqueadero:
                                archivo.write(placa + "\n")
                                print("Datos guardados en 'Registro_parqueadero.txt'.programa terminado ")
                    break
        else:
                    print("Opción inválida")
except ValueError:
    print("ERROR")
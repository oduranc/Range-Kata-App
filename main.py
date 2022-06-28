from range_oduranc import Range
import sys

def Menu(R1):
      print("\n1. Obtener todos los puntos." + 
            "\n2. Obtener los extremos." + 
            "\n3. Contiene números enteros." + 
            "\n4. Contiene otro rango." +
            "\n5. Volver a introducir rango." + 
            "\n6. Salir.")

      option = int(input("Seleccione la operación que desea realizar: "))
      Option(option, R1)

def Option(opt, R1):
    if opt == 1:
        result = Range.getAllPoints(R1)
    elif opt == 2:
        result = Range.endPoints(R1)
    elif opt == 3:
        nums = []
        nums = [number for number in input("Ingresa los números separados por espacio: ").split(" ")]
        convertedNums = map(lambda number: int(number), nums)
        
        result = Range.contains(R1, *list(convertedNums))
    elif opt == 4:
        R2 = input("Ingrese un nuevo rango: ")
        result = Range.containsRange(R1, R2)
    elif opt == 5:
            App()
    elif opt == 6:
            sys.exit()
        
    print(result)
    Menu(R1)

def App():
      strR1 = input("Introduzca un rango: ")
      R1 = Range(strR1)
      Menu(R1)

App()

# # R1 = Range('[2,6)')
# print(R1.getAllPoints())
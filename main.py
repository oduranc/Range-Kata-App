from Range_oduranc import Range

def Menu(R1):
      print("1. Obtener todos los puntos." + 
            "\n2. Obtener los extremos." + 
            "\n3. Contiene números enteros." + 
            "\n4. Contiene otro rango.")

      option = int(input("Seleccione la operación que desea realizar: "))
      Option(option, R1)

def Option(opt, R1):
    if opt == 1:
        result = Range.getAllPoints(R1)
    elif opt == 2:
        result = Range.endpoint(R1)
    elif opt == 3:
        nums = []
        nums = [number for number in input("Ingresa los números separados por espacio: ").split(" ")]
        convertedNums = map(lambda number: int(number), nums)
        
        result = Range.contains(R1, int(convertedNums))
    elif opt == 4:
        insertedRange = input("Ingrese un nuevo rango")
        R2 = Range(insertedRange)
        result = Range.containsRange(R1, R2)
        
    print(result)


strR1 = input("Introduzca un rango: ")
R1 = Range(strR1)
Menu(R1)

# # R1 = Range('[2,6)')
# print(R1.getAllPoints())
from range_oduranc import Range

def Menu(R1):
      print("1. Obtener todos los puntos." + 
            "\n2. Obtener los extremos." + 
            "\n3. Contiene números enteros." + 
            "\n4. Contiene otro rango.")

      option = int(input("Seleccione la operación que desea realizar: "))
      Option(option, R1)

def Option(opt, R1):
      match opt:
            case 1:
                  result = Range.getAllPoints(R1)
                  pass
            case 2:
                  result = Range.endPoints(R1)
                  pass
            case 3:
                  nums = []
                  nums = [int(number) for number in input("Ingresa los números separados por espacio: ").split()]
                  result = Range.contains(R1, list(nums))
                  pass
            case 4:
                  pass
      print(result)


strR1 = input("Introduzca un rango: ")
R1 = Range(strR1)
Menu(R1)

# # R1 = Range('[2,6)')
# print(R1.getAllPoints())
def main():
  
     materia1 = float(input("Calificación de la materia: "))
     materia2 = float(input("Calificación de la materia: "))
     materia3 = float(input("Calificación de la materia: "))
     materia4 = float(input("Calificación de la materia: "))
     promedio = (materia1 + materia2 + materia3 + materia4) / 4
     print ("El promedio es:",promedio)

#pytest assignments/03Promedio

if __name__ == '__main__':
    main()

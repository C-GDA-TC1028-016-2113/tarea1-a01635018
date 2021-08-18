def main():
    X1 = float(input("Dame x1: "))
    Y1 = float(input("Dame y1: ")) 
    X2 = float(input("Dame x2: "))
    Y2 = float(input("Dame y2: ")) 
    pendiente = (Y2 - Y1) / (X2 - X1)

    print("Pendiente:",pendiente)

#pytest assignments/07PendienteLinea
    

if __name__ == '__main__':
    main()

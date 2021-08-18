def main():
    peso_incial = float(input("Dame el peso inicial: "))
    peso_final = float(input("Dame el peso final: "))
    meses = int(input("Dame la cantidad de meses: "))
    kilos_mes = (peso_incial - peso_final) / meses 
    print("Lo que debes bajar por mes es:",kilos_mes)

#pytest assignments/06Peso


if __name__ == '__main__':
    main()

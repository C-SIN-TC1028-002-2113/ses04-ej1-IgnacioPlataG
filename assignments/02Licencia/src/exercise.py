def main():
    #escribe tu código abajo de esta línea
    Edad = int(input("Ingresa tu edad: "))
    if 0<Edad<18:
        print("No cumples requisitos") 
    elif Edad<=0:
        print("Respuesta incorrecta")
    else:
        ID = input("¿Tienes identificación oficial? (s/n): ")
        if ID=="s":
            print("Trámite de licencia concedido")
        elif ID=="n":
            print("No cumples requisitos")
        else:
            print("Respuesta incorrecta")
    

if __name__ == '__main__':
    main()

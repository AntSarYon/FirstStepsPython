def crearPiramideCentral(numeroNiveles):
    multiplicadorVacios = numeroNiveles-1
    multiplicadorEstrellas = 1

    for x in range(1, numeroNiveles+1, +1):
        print(" "*multiplicadorVacios, "*"*multiplicadorEstrellas, " "*multiplicadorVacios)
        multiplicadorVacios-=1
        multiplicadorEstrellas+=2
        
crearPiramideCentral(9)
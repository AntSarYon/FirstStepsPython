def hacerPiramideIzquierda(num):
    for x in range(1,num+1,+1):
        print("*"*x)

    for x in range(num-1,0,-1):
        print("*"*x)

hacerPiramideIzquierda(5)
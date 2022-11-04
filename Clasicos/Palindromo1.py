def esPalindromo(texto):

    esP = True

    listaOriginal = []
    for i in texto:
        listaOriginal.append(i)
    
    listaInversa = []
    for j in range(len(listaOriginal)-1,0,-1):
        listaInversa.append(listaOriginal[j])

    for x in range (0, len(listaOriginal)-1,+1):
        if listaOriginal[x] != listaInversa[x]:
            esP = False
            break
    
    if esP:
        print("Es Palindromo")
    else:
        print("No es Palindromo")

esPalindromo("mimamim")
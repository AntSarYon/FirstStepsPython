def esPalindromo(palabra):
    inv = len(palabra)-1
    esP = True
    for x in range(0, len(palabra)-1,+1):
        if(palabra[x] != palabra[inv]):
            esP = False
            break;
        else:
            inv-=1
    if esP==True:
        print("Es Palindromo")
    else:
        print("No es Palindromo")

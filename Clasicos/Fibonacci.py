def ObtenerFibonacci(num):
    if num == 1:
        return 0
    elif num == 2:
        return 1
    else:
        return ObtenerFibonacci(num-1) + ObtenerFibonacci(num-2)

print(ObtenerFibonacci(9))
def variables():
    tests = int(input())
    resp = []

    var = True
    while var is True:
        if tests<1 or tests>100:
            test = int(input("Test debe ser mayor que 1 y menor que 100: "))
        else:
            var = False
            
    for i in range(tests):
        nk = input()
        cadena = input()
        serie = []

        i = 0
        x = 0
        while nk[i] != " ":
            i += 1

        n = int(nk[:i])
        k = int(nk[i+1:])

        var = True
        while var is True:
            if k<1 or k>7:
                k = int(input("K debe ser mayor que 1 y menor que 7: "))
            else:
                var = False

        var = True
        while var is True:
            if n<k or n>1000:
                n = int(input("N debe ser mayor que K y menor que 1000: "))
            else:
                var = False

        var = True
        while var is True:
            if len(cadena) != n:
                print("El valor dado debe ser de",n,"digitos de longitud: ")
                cadena = input()
            else:
                var = False

        i = 0
        for i in range(n):
            serie.append(int(cadena[i]))

        resp.append(main(n,k,serie))

    for i in resp:
        print(i)


def main(n,k,serie):
    x = 0
    i = 0
    mult = 1
    valores = []
    while (x+k) <= n:
        while i < k:
            mult = mult*serie[x+i]
            i += 1
        valores.append(mult)
        i = 0
        mult = 1
        x += 1

    valores.sort()

    return(valores[-1])

def pruebas(tests,n,k,cadena):
    resp = []
    serie = []
    cadena = str(cadena)

    var = True
    while var is True:
        if tests<1 or tests>100:
            test = int(input("Test debe ser mayor que 1 y menor que 100: "))
        else:
            var = False

    var = True
    while var is True:
        if k<1 or k>7:
            k = int(input("K debe ser mayor que 1 y menor que 7: "))
        else:
            var = False

    var = True
    while var is True:
        if n<k or n>1000:
            n = int(input("N debe ser mayor que K y menor que 1000: "))
        else:
            var = False

    var = True
    while var is True:
        if len(cadena) != n:
            print("El valor dado debe ser de",n,"digitos de longitud: ")
            cadena = input()
        else:
            var = False
            
    i = 0
    for i in range(n):
        serie.append(int(cadena[i]))

    return(main(n,k,serie))

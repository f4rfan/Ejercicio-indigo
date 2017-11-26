def main():
    rsp = ''
    resp = []
    while rsp != 'N' and rsp != 'n':
        tests = int(input())
        var = True
        while var is True:
            if tests<1 or tests>100:
                test = int(input("Test debe ser mayor que 1 y menor que 100: "))
            else:
                var = False
        for i in range(tests):
            resp.append(func())

        for i in resp:
            print('\n',resp[i])
            
        rsp = input("Desea volver a intentarlo? \nS/N: ")


def func():
    n_char = input()
    n = int(n_char)
    serie = []
    valores = []

    var = True
    while var is True:
        if 101101 > n or n > 1000000:
            n = int(input("N debe ser mayor que 101101 y menor que 1000000: "))
        else:
            var = False

    for i in range(100,1000):
        for x in range(100,1000):
            if (i*x) <= n and (i*x) >= 101101:
                if (i*x) not in serie:
                    serie.append(i*x)

    serie.sort()

    print(serie)

    for i in serie:
        valores.append(str(i))

    print(valores)

    var = True
    i = len(valores)-1
    while var == True:
        if valores[i][:3] == valores[i][3:]:
            var = False
        else:
            i -= 1

    return(serie[i])

main()

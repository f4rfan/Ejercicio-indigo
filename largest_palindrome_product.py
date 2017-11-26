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
            print(i)
            
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
                valor = str(i*x)
                if valor[:3] == valor[-1:-4:-1]:
                    if (i*x) not in serie:
                        serie.append(i*x)

    serie.sort()
    
    return(serie[-1])

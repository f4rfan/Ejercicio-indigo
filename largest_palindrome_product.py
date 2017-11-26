def variables():
    test = int(input())
    resp = []
        
    var = True
    while var is True:
        if test<1 or test>100:
            test = int(input("Test debe ser mayor que 1 y menor que 100: "))
        else:
            var = False
  
    for i in range(test):
        n = int(input())
        var = True
        while var is True:
            if 101101 > n or n > 1000000:
                n = int(input("N debe ser mayor que 101101 y menor que 1000000: "))
            else:
                var = False

        resp.append(main(n))

    for i in resp:
        print(i)


def main(n):
    serie = []

    for x in range(100,1000):
        for y in range(100,1000):
            valores =[]
            if (x*y) <= n and (x*y) >= 101101:
                valor = str(x*y)
                if valor[:3] == valor[-1:-4:-1]:
                    if (x*y) not in serie:
                        valores = [x*y,x,y]
                        serie.append(valores)

    serie.sort()

    return(serie[-1])

def pruebas(test,n):
    resp = []
    
    var = True
    while var is True:
        if test<1 or test>100:
            test = int(input("Test debe ser mayor que 1 y menor que 100: "))
        else:
            var = False
  
    var = True
    while var is True:
        if 101101 > n or n > 1000000:
            n = int(input("N debe ser mayor que 101101 y menor que 1000000: "))
        else:
            var = False

    return(main(n))

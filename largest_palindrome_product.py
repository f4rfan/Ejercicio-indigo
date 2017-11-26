def main():
    rsp = ""
    resp = []
    nn = ["N","n"]
    while rsp not in nn :
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
            
        rsp = input("Desea volver a intentarlo?\nS/N:")


def func():
    n1 = int(input())
    serie = []
    valores = []

    var = True
    while var is True:
        if 101101 > n1 or n1 > 1000000:
            n1 = int(input("N debe ser mayor que 101101 y menor que 1000000: "))
        else:
            var = False

    for i in range(100,1000):
        for x in range(100,1000):
            valores =[]
            if (i*x) <= n1 and (i*x) >= 101101:
                valor = str(i*x)
                if valor[:3] == valor[-1:-4:-1]:
                    if (i*x) not in serie:
                        valores = [i*x,i,x]
                        serie.append(valores)

    serie.sort()
    
    return(serie[-1])

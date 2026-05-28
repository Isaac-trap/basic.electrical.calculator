import math
def SacarDatos():
    print("como usar prefijos...")    
    print("Mega = M, Kilo = K")
    print("mili = m, micro = u")
    print("define 2 valores, los desconocidos con 0")

    R = input("define valor R: ")
    V = input("define valor V: ")
    I = input("define valor I: ")
    P = input("define valor P: ")
    return (R, V, I, P)

def Multisub(R, V, I, P):
    resultados = []
    for i in (R, V, I, P):
        if i[-1] == "M":
            factor = 1000000
            valor = i[:-1]
            resultados.append(float(valor) * factor)
        elif i[-1] == "K":
            factor = 1000
            valor = i[:-1]
            resultados.append(float(valor) * factor)
        elif i[-1] == "m":
            factor = 0.001
            valor = i[:-1]
            resultados.append(float(valor) * factor)
        elif i[-1] == "u":
            factor = 0.000001
            valor = i[:-1]
            resultados.append(float(valor) * factor)
        elif i[-1] not in ["M", "K", "m", "u"] and not i[-1].isdigit():
            print("la terminacón")
            print(i[-1])
            print("no esta integrada o no corresponde")
            break
        else:
            resultados.append(float(i))
    return (resultados)

def OP(R ,V , I, P):
    com = []
    com2 = []
    result = []
    for i in (R ,V , I, P):
        if i == 0.0:
            com.append(i)
        else:
            com2.append(i)
    if com == [R,V]:
        V = P/I
        R = V/I
        result.append((R, V, I, P))
    elif com == [R,I]:
        I = P/V
        R = V/I
        result.append((R,V,I,P))
    elif com == [R,P]:
        R = V/I
        P = V*I
        result.append((R,V,I,P))
    elif com == [V,I]:
        V = math.sqrt(P*R)
        I = V/R
        result.append((R,V,I,P))
    elif com == [V,P]:
        V = I*R
        P = V*I
        result.append((R,V,I,P))
    elif com == [I,P]:
        I = V/R
        P = I*V
        result.append((R,V,I,P))
    elif com == [V]:
        V = I*R
        result.append((R,V,I,P))
    elif com == [I]:
        I = V/R
        result.append((R,V,I,P))
    elif com == [R]:
        R = V/I
        result.append((R,V,I,P))
    elif com == [P]:
       P = I*V
       result.append((R,V,I,P))
    return print(result)
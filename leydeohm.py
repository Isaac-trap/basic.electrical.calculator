import math

def sacar_todo():
    print("como usar prefijos...")
    print("Mega = M, Kilo = K")
    print("mili = m, micro = u")
    print("unidad = valor/representación")
    R = input("define valor R:")
    V = input("define valor V:")
    I = input("define valor I:")
    P = input("define valor P:")

    if R[-1].isdigit():
        NR = float(R)
    else:
        NR = float(R[:-1])
    if V[-1].isdigit():
        NV = float(V)
    else:
        NV = float(V[:-1])
    if I[-1].isdigit():
        NI = float(I)
    else:
        NI = float(I[:-1])    
    if P[-1].isdigit():
        NP = float(P)
    else:
        NP = float(P[:-1])
# MULTIPLOS/SUB evalua el prefijo para luego operar con el valor en unidad
    
    if R[-1] == "K":
        multiplo_NR = 1000
    elif R[-1] == "M":
        multiplo_NR = 1000000
    elif R[-1] != "K" or "M":
        multiplo_NR = 1
    if R[-1] == "m":
        submultiplo_NR = 1000
    elif R[-1] == "u":
        submultiplo_NR = 1000000
    elif R[-1] != "m" or "u":
        submultiplo_NR = 1

    if V[-1] == "K":
        multiplo_NV = 1000
    elif V[-1] == "M":
        multiplo_NV = 1000000
    elif V[-1] != "K" or "M":
        multiplo_NV = 1
    submultiplo_NV = 1
    if V[-1] == "m":
        submultiplo_NV = 1000
    elif V[-1] == "u":
        submultiplo_NV = 1000000
    elif V[-1] != "m" or "u":
        submultiplo_NV = 1
    
    if I[-1] == "K":
        multiplo_NI = 1000
    elif I[-1] == "M":
        multiplo_NI = 1000000
    elif I[-1] != "K" or "M":
        multiplo_NI = 1
    submultiplo_NI = 1
    if I[-1] == "m":
        submultiplo_NI = 1000
    elif I[-1] == "u":
        submultiplo_NI = 1000000
    elif I[-1] != "m" or "u":
        submultiplo_NI = 1

    if P[-1] == "K":
        multiplo_NP = 1000
    elif P[-1] == "M":
        multiplo_NP = 1000000
    elif P[-1] != "K" or "M":
        multiplo_NP = 1
    submultiplo_NP = 1
    if P[-1] == "m":
        submultiplo_NP = 1000
    elif P[-1] == "u":
        submultiplo_NP = 1000000
    elif P[-1] != "m" or "u":
        submultiplo_NP = 1

#SACAR DATOS segun los datos que allas dejado con 0 va a calcular su valor con los datos que determinaste

    if NI == 0.0 and NP == 0.0:
        newI = (NV*multiplo_NV/submultiplo_NV)/(NR*multiplo_NR/submultiplo_NR)
        newP = (NV*multiplo_NV/submultiplo_NV)*newI
        print("I:",newI,"P:",newP)
    elif NV == 0.0 and NI == 0.0:
        newV = math.sqrt((NP*multiplo_NP/submultiplo_NP)*(NR*multiplo_NR/submultiplo_NR))
        newI = newV/(NR*multiplo_NR/submultiplo_NR)
        print("V:",newV,"I:",newI)
    elif NR == 0.0 and NI == 0.0:
        newI = (NP*multiplo_NP/submultiplo_NP)/(NV*multiplo_NV/submultiplo_NV)
        newR = (NV*multiplo_NV/submultiplo_NV)*newI
        print("I:",newI,"R:",newR)
    elif NR == 0.0 and NP == 0.0:
        newR = (NV*multiplo_NV/submultiplo_NV)/(NI*multiplo_NI/submultiplo_NI)
        newP = (NV*multiplo_NV/submultiplo_NV)*(NI*multiplo_NI/submultiplo_NI)
        print("R:",newR,"P:",newP)
    elif NR == 0.0 and NV == 0.0:
        newV = (NP*multiplo_NP/submultiplo_NP)/(NI*multiplo_NI/submultiplo_NI)
        newR = newV/(NI*multiplo_NI/submultiplo_NI)
        print("R:",newR,"V:",newV)
    elif NV == 0.0 and NP == 0.0:
        newV =(NI*multiplo_NI/submultiplo_NI)*(NR*multiplo_NI/submultiplo_NI)
        newP =(NI*multiplo_NI/submultiplo_NI)*newV 
        print("V:",newV,"P:",newP)

#bucle en el que confirmas si continuaras usando el programa

def continuar():
    print("¿continuar?")
    print("Y/N")
    deseo = input(": ")
    return deseo

a = continuar()
while a.upper() != "N":
    sacar_todo()
    a = continuar()
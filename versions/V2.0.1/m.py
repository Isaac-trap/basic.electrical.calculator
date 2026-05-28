import p as Red
while 1 : 
    continuar = input("continuar?: ")
    if continuar == "n":
        break
    else:
        Val_N = Red.SacarDatos()

        RN = Val_N[0]
        VN = Val_N[1]
        IN = Val_N[2]
        PN = Val_N[3]

        Val_C = Red.Multisub(RN, VN, IN, PN)

        RC = Val_C[0]
        VC = Val_C[1]
        IC = Val_C[2]
        PC = Val_C[3]

        Red.OP(RC, VC, IC, PC)
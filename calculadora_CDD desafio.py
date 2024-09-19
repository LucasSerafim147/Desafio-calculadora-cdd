
while True:

    n1 = float(input("Insira o primeiro numero: "))
    n2 = float(input("Insira o segundo numero: "))

    op = int(input("1-Adição\n2-Subtração\n3-Divisão\n4-Multiplicação\n5-Tentar outro numero\n6-Sair\nInsira:"))

    if op == 1:
        resultado = n1 + n2
        print(resultado)
        op == 5
    elif op == 2 :
        resultado = n1 - n2
        print(resultado)
        op == 5
    elif op == 3 :
        resultado = n1 / n2
        print(resultado)
        op == 5
    elif op == 4:
        resultado = n1 * n2
        print(resultado)
        op == 5
    elif op == 5:
        
        continue
    elif op ==6:
        break
       

        

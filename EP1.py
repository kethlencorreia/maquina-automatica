def troco(x):
    if x>=100:
        print("R$100,00")
        return troco(x-100)
    elif x>=50:
        print("R$50,00")
        return troco(x-50)
    elif x>=20:
        print("R$20,00")
        return troco(x-20)
    elif x>=10:
        print("R$10,00")
        return troco(x-10)
    elif x>=5:
        print("R$5,00")
        return troco(x-5)
    elif x>=2:
        print("R$2,00")
        return troco(x-2)
    elif x>=1:
        print("R$1,00")
        return troco(round(x-1,2))
    elif x>=0.50:
        print("R$0,50")
        return troco(round(x-0.50,2))
    elif x>=0.25:
        print("R$0,25")
        return troco(round(x-0.25,2))
    elif x>=0.10:
        print("R$0,10")
        return troco(round(x-0.10,2))
    elif x>=0.05:
        print("R$0,05")
        return troco(round(x-0.05,2))
    elif x>=0.01:
        print("R$0,01")
        return troco(round(x-0.01,2))

def valor(a,b):
    if a>=b:
        print("")
        print("Valor pago: R${}".format(a))
        print("Troco:R${}".format(round(a-b,2)))
        print("")
        print("Pegue seu troco: ")
        troco(round(a-b,2))
        return a
    else:
        c=float(input("Coloque o seu dinheiro: "))
        return valor(a+c,b)


def produtos(p1=1,p2=1,p3=1,p4=1,p5=1):
    if p1==0 and p2==0 and p3==0 and p4==0 and p5==0:
        print("Desculpa, mas a maquina está sem produtos")
        return exit()
    print("------------------------------------------")
    if p1>0:
        print("1 - Cigarro       -R$7,84     {}".format(p1))
    else:
        print("1 - Cigarro       -Indisponivel")
    if p2>0:
        print("2 - Pepsi 350ml   -R$2,49     {}".format(p2))
    else:
        print("2 - Pepsi 350ml   -Indisponivel")
    if p3>0:
        print("3 - Chocolate     -R$3,34     {}".format(p3))
    else:
        print("3 - Chocolate     -Indisponivel")
    if p4>0:
        print("4 - Batata        -R$6,57     {}".format(p4))
    else:
        print("4 - Batata        -Indisponivel")
    if p5>0:
        print("5 - Bala Fini     -R$3,75     {}".format(p5))
    else:
        print("5 - Bala Fini     -Indisponivel")
    print("------------------------------------------")

    r=int(input("Escolha o seu produto: "))
    if r==1:
        preço=7.99
        if p1==0:
            print("Cigarro está Indisponivel")
            print("")
            g = input("Você deseja comprar outro produto? S/N ")
            print("")
            if g == "s" or g == "S":
                produtos(p1,p2,p3,p4,p5)
            elif g == "n" or g == "N":
                print("Volte sempre")
                exit()
        print("Você escolheu Cigarro ")
        print("Preço: R$7,84")
        print("")
        dinheiro = float(input("Coloque o seu dinheiro: "))
        valor(dinheiro, preço)
        print("")
        g = input("Você deseja comprar outro produto? S/N ")
        if g == "s" or g == "S":
            return produtos(p1-1, p2, p3, p4, p5)
        elif g == "n" or g == "N":
            print("Volte sempre")
            exit()


    elif r==2:
        preço = 2.49
        if p2==0:
            print("Pepsi 350ml está Indisponivel")
            print("")
            g = input("Você deseja comprar outro produto? S/N ")
            if g == "s" or g == "S":
                produtos(p1,p2,p3,p4,p5)
            elif g == "n" or g == "N":
                print("Volte sempre")
                exit()
        print("Você escolheu Pepsi 350ml")
        print("Preço: R$2,49")
        print("")
        dinheiro = float(input("Coloque o seu dinheiro: "))
        valor(dinheiro,preço)
        print("")
        g = input("Você deseja comprar outro produto? S/N ")
        if g == "s" or g == "S":
            return produtos(p1, p2-1, p3, p4, p5)
        elif g == "n" or g == "N":
            print("Volte sempre")
            exit()




    elif r==3:
        preço=3.34
        if p3==0:
            print("Chocolate está Indisponivel")
            print("")
            g = input("Você deseja comprar outro produto? S/N ")
            if g == "s" or g == "S":
                produtos(p1,p2,p3,p4,p5)
            elif g == "n" or g == "N":
                print("Volte sempre")
                exit()
        print("Você escolheu Chocolate")
        print("Preço: R$3,34")
        print("")
        dinheiro = float(input("Coloque o seu dinheiro: "))
        valor(dinheiro, preço)
        print("")
        g = input("Você deseja comprar outro produto? S/N ")
        if g == "s" or g == "S":
            return produtos(p1, p2, p3-1, p4, p5)
        elif g == "n" or g == "N":
            print("Volte sempre")
            exit()

    elif r==4:
        preço=6.57
        if p4==0:
            print("Batata está Indisponivel")
            print("")
            g = input("Você deseja comprar outro produto? S/N ")
            if g == "s" or g == "S":
                produtos(p1,p2,p3,p4,p5)
            elif g == "n" or g == "N":
                print("Volte sempre")
                exit()
        print("Você escolheu Batata ")
        print("Preço: R$6,57")
        print("")
        dinheiro = float(input("Coloque o seu dinheiro: "))
        valor(dinheiro, preço)
        print("")
        g = input("Você deseja comprar outro produto? S/N ")
        if g == "s" or g=="S":
            return produtos(p1,p2,p3,p4-1,p5)
        elif g== "n" or g=="N":
            print("Volte sempre")
            exit()

    elif r==5:
        preço=3.75
        if p5==0:
            print("Bala Fini está Indisponivel")
            print("")
            g = input("Você deseja comprar outro produto? S/N ")
            if g == "s" or g == "S":
                produtos(p1,p2,p3,p4,p5)
            elif g == "n" or g == "N":
                print("Volte sempre")
                exit()
        print("Você escolheu Bala Fini")
        print("Preço: R$3,75")
        print("")
        dinheiro = float(input("Coloque o seu dinheiro: "))
        valor(dinheiro, preço)
        print(" ")
        g = input("Você deseja comprar outro produto? S/N ")
        if g == "s" or g == "S":
            return produtos(p1, p2, p3, p4, p5-1)
        elif g == "n" or g == "N":
            print("Volte sempre")
            exit()


    elif r<0 or r>5:
        print("Digite um número correspondente a um produto!")
    print("  ")
    g=input("Você deseja comprar mais algum produto? S/N ")
    if g=="s" or g=="S":
        produtos(p1,p2,p3,p4,p5)
    elif g == "n" or g == "N":
        print("Volte sempre")
        exit()

def main():
    produtos()
main()


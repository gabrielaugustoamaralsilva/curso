while True:
 p = int(input("digite sua idade:"))

 if p>14 and p<18:
    print("voce tem acesso limitado a essa rede social")

 if p<14:
    print("voce nao tem acesso a essa rede social")

 if p>=18:
    print("voce tem acesso total a essa rede social")
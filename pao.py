User = {}
while True:
 p = int(input("digite sua idade:"))

 if p>14 and p<18:
    print("voce tem acesso limitado a esse banco ")

 if p<14:
    print("voce nao tem acesso a esse banco ")
    break

 if p>=18:
    print("voce tem acesso total a esse banco ")
 
 name = input("Digite seu nome: ")

 begin = input(f"Seja bem vindo {name}, qual será a sua primeira operação, saque ou deposito? " )


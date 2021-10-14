import random
class ERRORMENOS(Exception):
    'El nombre es menor'
    pass
class ERROMES(Exception):
    'El nombre es major'
    pass
num1=random.randint(0,101)
print(num1)
i=1
while i!=0:

    num=input("Donam el nombre ")
    num=int(num)
    if num1>num:
        print("Es major")
        raise ERRORMENOS
        throw 
    if num>num1:
        print("Es menor")
        raise ERROMES        
    if num1==num:
        print("Felicitacions has obtigut el nombre que desijabes")
        break

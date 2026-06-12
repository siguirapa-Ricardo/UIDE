# Validar si es mayor o menor de edad


"""edad = int(input("Ingrese su edad: "))
if edad >= 18 and edad < 65:
    print("Es mayor de Edad")
if edad >= 66:
    print("Es Adulto mayor de Edad")
if edad < 1:
    print("Es recien nacido ")
if edad >=1 and edad < 18:
    print("Es menor de edad")
    
    tres iguales o son diferentes """


n1 = int(input("Ingrese el Numero 1: "))
n2 = int(input("Ingrese el Numero 2: "))
n3 = int(input("Ingrese el Numero 3: "))

if n1==n2 and n2==n3 and n1==n3:
    print("Los numeros son iguales ")
else:
    print("Los numero ingresados son diferentes pero ")
    if (n1==n2 or n1==n3) and (n2==n3 or n2==n1):
        print("El numero 1: ",n1,"El nuemro 2 :",n2,"Son igaules diferente al numero 3: ")
    if (n2==n1 or n2==n3) and (n3==n1 or n3==n2):
        print("El numero 2: ",n2,"El nuemro 3 :",n3,"Son igaules diferente al numero 1 :")
    if (n3==n1 or n3==n2) and (n1==n2 or n1==n3):
        print("El numero 3: ",n3,"El nuemro 1 :",n1,"Son igaules diferente al numero 2 :")

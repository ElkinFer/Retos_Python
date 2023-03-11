print ("Bienvenido a su cuenta")

cont = "s"
cuenta = 1000000

while cont == "s" or cont =="S":
    print ("Saldo inicial", cuenta)
    oper = int(input ("Para consignar oprima 1, para retirar oprima 2 \n"))
    
    if oper == 1:
        consig = int(input ("digite el valor a consignar: \n"))
        cuenta = cuenta + consig
        
    else: 
        oper == 2
        retiro = int(input("ingrese el valor a retirar \n")) 
        cuenta = cuenta - retiro
    cont = input("Desea hacer otra operación? marque s para continuar o cualquier tecla para salir:\n") 
        
    print ("Su nuevo saldo es: \n", cuenta)   
       
        
 
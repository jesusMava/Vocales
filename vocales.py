#Progrma para las vocales
def CuentaVocales(cadena):
	cont=0
	contE=0
	contI=0
	contO=0
	contU=0
	for letra in cadena:
		if(letra=="A") or(letra=="a"):
			cont=cont+1
		elif (letra=="E")or(letra=="e"): 
			contE=contE+1
	        elif(letra=="I")or(letra=="i"):
			contI=contI+1
	        elif(letra=="O")or(letra=="o"):
			contO=contO+1
		elif(letra=="U")or(letra=="u"):
			contU=contU+1
	print "A : ",cont
	print "E : ",contE
	print "I : ",contI
	print "O : ",contO
	print "U : ",contU
	print "Total vocales : ",cont+contE+contI+contO+contU

x = raw_input("Introduce la cadena: ")
CuentaVocales(x)

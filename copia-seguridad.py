# -*- coding: utf-8 -*-
import turtle
import os

#MAIN
def main():

	os.system('cls')
	getform = input('¿Que forma deseas hacer?\n1.-Rectangulo.\n2.-Triangulo.\n3.-Cuadrado.\n4.-Nada.\nDecide ahora:')
	getform = cambio_type(getform)
	getform = verificar_getform(getform)

	window = turtle.Screen()

	if (getform == 1):
		form='Rectangulo'
		welcome(form)
		make_form(form)
	elif (getform == 2):
		form='Triangulo'
		welcome(form)
		make_form(form)
	elif (getform == 3):
		form='Cuadrado'
		welcome(form)
		make_form(form)
	elif (getform == 4):
		form='Nada'
		welcome(form)
		print('Nada')

	window = turtle.Screen()
	turtle.mainloop()



#BORRADOR DE PANTALLA Y BIENVENIDA
def welcome(form):
	os.system('cls')
	if(form == 'Nada'):
	 print('Usted no ha seleccionado nada')
	 exit()
	else:
	 print('Bienvenidos al Artista de formas usted ha seleccionado dibujar un ' + form)

# CAMBIO DE TIPO
def cambio_type(value):
	try:
		value = int(value)
		return value
	except:
		print('\nIngresó un caracter o string.Vuelva a intentarlo\n')
		value = None
		return value


#SELECCIONADOR DE FORMA
def make_form(form):
	if (form == 'Rectangulo'):
		make_rectangule(form)
	if (form == 'Triangulo'):
		make_triangle(form)
	if (form == 'Cuadrado'):
		make_square(form)
	if (form == 'Nada'):
		exit() 



# LIMPIAR PANTALLA
def limpiar_pantalla(intentos):
	comprobacion= intentos % 2
	if((comprobacion == 0) or (intentos == 1)):
		os.system('cls')



# DIBUJADOR DE RECTANGULO
def make_rectangule(form):
	welcome(form)
	contador_intentos=0
	angulo = 90
	# PEDIMOS BASE
	base= input('\nIngrese el valor de la base del ' + form + '\nIngrese ahora:')
	#CAMBIAMOS DE STR A INT
	base=cambio_type(base)
	#VERIFICAMOS SI SE PUEDO REALIZAR EL CAMBIO Y  QUE SEA MAYOR QUE 0
	base = verificar_value(form,'base',base)

	#PEDIMOS ALTURA
	altura= input('\nIngrese el valor de la altura del ' + form + '\nIngrese ahora:')
	#CAMBIAMOS DE STR A INT
	altura=cambio_type(altura)
	#SI ALTURA RESULTA SER INT
	while(altura == None):
		altura=verificar_value(form,'altura',altura)
	else:
	    #SI LA ALTURA ES IGUAL A LA BASE
		while((base == altura) or (altura <= 0)):
		    #SE ENVIA UN ERROR
			if (base == altura):
				error='\nLa base y la altura son de la misma longitud.'
			elif(altura <= 0):
				error='\nLa altura menor a 0.'
			    #SE VERIFICA EL VALOR SI ES MAYOR A 0 Y QUE SEA INT
			altura=verificar_value(form,'altura',altura,error)

	lapiz = turtle.Turtle()

	lados= 4

	for contador_lados in range(lados):
		lado_rectangulo= contador_lados % 2
		if(lado_rectangulo == 0):
			make_line(lapiz,base)
			lapiz.left(angulo)
		else:
			make_line(lapiz,altura)
			lapiz.left(angulo)


# DIBUJADOR DE TRIANGULO
def make_triangle(form):
	welcome(form)
	contador_intentos=0
	angulo = 120
	# PEDIMOS LADOS
	lado= input('\nIngrese el valor de la longitud de los lados del ' + form + '\nIngrese ahora:')
	#CAMBIAMOS DE STR A INT
	lado=cambio_type(lado)
	#VERIFICAMOS SI SE PUEDO REALIZAR EL CAMBIO Y  QUE SEA MAYOR QUE 0
	lado= verificar_value(form,'longitud de los lados',lado)

	lapiz = turtle.Turtle()

	lados= 3
	for contador_lados in range(lados):
		make_line(lapiz,lado) 
		lapiz.left(angulo)

def make_square(form):
	welcome(form)
	contador_intentos=0
	angulo = 90
	lado= input('\nIngrese el valor de los lados del ' + form + '\nIngrese ahora:')
	lado=cambio_type(lado)
	lado= verificar_value(form,'longitud de los lados',lado)
	
	lapiz = turtle.Turtle()

	lados= 4

	for contador_lados in range(lados):
		make_line(lapiz,lado)
		lapiz.left(angulo)


# DIBUJADOR DE LINEA
def make_line(lapiz,length):
	lapiz.forward(length)

#VERIFICADOR DE FORM
def verificar_getform(getform,contador_intentos = None):
	if (contador_intentos == None):
		contador_intentos = 0
	try:
		while ( ( type(getform) != int) or (getform > 5) or (getform < 1)):
			getform = input('\nOpcion no encontrada.\n¿Que forma deseas hacer?\n1.-Rectangulo.\n2.-Triangulo.\n3.-Cuadrado.\n4.-Nada.\nDecide ahora:')
			getform = cambio_type(getform)
			contador_intentos = contador_intentos + 1
			limpiar_pantalla(contador_intentos)
			if(getform):
				if ((type(getform) != int) and (getform < 5) and (getform > 1)):
					return getform
		else:
			return getform

	except:
		while (getform == None):
			getform = input('\nOpcion no encontrada.\n¿Que forma deseas hacer?\n1.-Rectangulo.\n2.-Triangulo.\n3.-Cuadrado.\n4.-Nada.\nDecide ahora:')
			getform = cambio_type(getform)
			contador_intentos = contador_intentos + 1
			limpiar_pantalla(contador_intentos)
			if (getform):
				if ((type(getform) != int) and (getform < 5) and (getform > 1)):
					return verificar_getform(getform,contador_intentos)

#VERIFICADOR VALOR
def verificar_value(form,atributo,value = None,error = None,contador_intentos = None):
	if (contador_intentos == None):
		contador_intentos = 0
	try:
		while ((value<=0) or (error) or (type(value) != int)):
			if (error):
				print(error)
			else:
				print('\nValor es igual o menor que 0 intente de nuevo.')
			value= input('\nIngrese el valor de la ' + atributo + ' del ' + form + '\nIngrese ahora:')
			value=cambio_type(value)
			contador_intentos = contador_intentos + 1
			limpiar_pantalla(contador_intentos)
			if(value):
				if((value > 0) and (type(value) == int)):
					error = None
					return value
		else:
			return value
	except:
		while ((value == None) or (error) or (type(value) != int) or (value<=0)):
			print('\nValor Invalido. Vuelva a intentarlo.')
			value= input('\nIngrese el valor de la ' + atributo + ' del ' + form + '\nIngrese ahora:')
			value=cambio_type(value)
			contador_intentos = contador_intentos + 1
			limpiar_pantalla(contador_intentos)
			if(value):
				if((value > 0) and (type(value) == int)):
					error = None
					return value
			else:
				return verificar_value(form,atributo,value,error,contador_intentos)
	

if __name__ == '__main__':
	main()

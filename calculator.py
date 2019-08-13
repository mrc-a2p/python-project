def dividir(variable1,variable2):
   operacion_dividir = round(variable1/variable2) #round es redondear decimales
   return operacion_dividir
 
##########################
# creacion de un funcion con la palabra reservada  DEF ,
#  nombre que se quiera asignar y 505
# le pasamos los parametros deseados

def indice():
#Interaccion con el usuario 
    print('calacola')
    variable1 = float(input('Primer numero:'))
    variable2 = float(input('Segundo numero:'))

# Ejecuto funciones 
    resultado_final = dividir(variable1,variable2)
    print (resultado_final)

#.#########################
if __name__ == '__main__':
    indice()

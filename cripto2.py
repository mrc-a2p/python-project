

### programa que encripta y desencripta frases segùn una clave arbitraria

dictio = {"a":"B", "b":"C", "c":"D", "d":"E", "e":"F", "f":"G", "g":"H", "h":"I", "i":"J", "j":"K", "k":"L", "l":"M",
            "m":"N", "n":"O", "o":"P", "p":"Q", "q":"R", "r":"S", "s":"T", "t":"U", "u":"V", "v":"W", "w":"X", "x":"Y",
            "y":"Z", "z":"A", "ll":"Ñ", "ñ":"LL", " ":" "}

def listaLetras(lista):
    letras = []
    for i in lista:
        straux = i
        for j in straux:
            letras.append(j)
        letras.append(" ")
    return letras
    

def codificar(mensaje):
    letras = []; mEncr = []; cadEncr = ""
    mensaje=mensaje.lower()
    palabras = mensaje.split() ## palabras es lista que contiene las palabras del mensaje a codificar
    ##print (type (palabras), len (palabras), palabras)
    
    letras = listaLetras (palabras)
    ##print(letras)
    for i in letras:
        mEncr.append(dictio[i]) ## mEncr lista que contiene letras del mensaje encriptado, con espacios
    
    cadEncr = cadEncr.join(mEncr)
    print ("Mensaje encriptado: ", cadEncr)
    

def decodificar(mEncr):
    letrasE = []; msj = []; cadMsj = ""; straux = ""
    palabrasE = mEncr.split()
    
    letrasE = listaLetras (palabrasE)
    for i in letrasE:
        for k, v in dictio.items():
            if v==i:
                msj.append(k)    
    cadMsj = cadMsj.join(msj)
    print ("Mensaje decriptado: ", cadMsj)


def inicio():
    op = 0
    while op != 3:
        print ("\n\n\t\t··Programa (de)codificador··\n\tIngrese opción: \n")
        op = int(input("\t Codificar mensaje (1)\n\t Decodificar (2)\n\t Salir (3)\t"))
        if op == 1:
            mensaje = input("\tIngrese mensaje a codificar: ")
            codificar (mensaje)
        elif op == 2:
            mEncriptado = input ("\tIngrese mensaje encriptado para decodificarlo: ")
            decodificar (mEncriptado)

inicio()
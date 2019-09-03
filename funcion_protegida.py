
def protect(func):
    def wrapper(password):
        if password == "platzi":
            return func()
        else:
            print ("La contraseña es incorrecta")
    
    return wrapper 


@protect
def protect_func(): 
    print("Tu contraseña es correcta.")



if __name__ == '__main__':
    password = str(input("Ingresa la contraseña: "))

    
    protect_func(password)


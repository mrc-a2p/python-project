import turtle   


def main(): 
    window = turtle.Screen()         
    window.setup(350, 350, 0, 0) #TAMAÑO VENTANA 
    window.title("Ejemplo de ventana")
    #window.screensize(300, 300)

    # turtle.dot(10, 0, 0, 0)
    dave = turtle.Turtle()
    #dave = turtle.hideturtle()


    #turtle.goto(50, 30)
    turtle.pencolor("red")




    make_square(dave)
#Mantiene la ventana abierta 
    turtle.mainloop()


def make_square(dave):
        #Poner en la consola los grados que necesites
    lenght = int(input('Tamaño de cuadrado: '))
    
    for i in range(4):
        make_line_and_turn(dave, lenght)

def make_line_and_turn(dave, lenght):
    dave.forward(lenght)
    dave.left(90)
    dave.pencolor("blue")
    #dave.goto(50, 10)



# def camino_tortuga(dave):
#     dave.penup()
#     dave.goto(100, 50)
#     dave.dot(10, 255, 0, 0)
    # turtle.goto(100, 50)
    # turtle.dot(10, 255, 0, 0)

    
      

if __name__== '__main__':
   main()

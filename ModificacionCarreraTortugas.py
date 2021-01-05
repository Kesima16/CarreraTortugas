import turtle
import random

class Circuito():
    corredores = []
    __Ncorredores = 0
    __posStartY = (-30,-10, 10, 30)
    __colorTurtle = ('red', 'blue', 'green', 'orange')
    
    def __init__(self, width, height):
        self.__screen = turtle.Screen()
        self.__screen.setup(width, height)
        self.__screen.bgcolor('lightgray')
        self.__startline = -(width/2 - 20)
        self.__finishline = width/2 -20
        
        
    def __createRunners(self):
        for i in range(self.__Ncorredores):
            new_turtle = turtle.Turtle()
            new_turtle.shape('turtle')
            new_turtle.penup()
            new_turtle.color(self.__colorTurtle[i])
            new_turtle.setpos(self.__startline, self.__posStartY[i])
            
            self.corredores.append(new_turtle)
     
    def participan(self, *nombre):
        if nombre == None:
            print("Participan {} corredores".format(self.__Ncorredores))
    
        else:
            self.__Ncorredores=len(nombre)
            print("Participan {} corredores".format(self.__Ncorredores))
            
        self.__createRunners()
    
     
    def competir(self):
        hayGanador = False
        
        while not hayGanador:
            for tortuga in self.corredores:
                avance = random.randint(1, 6)
                tortuga.fd(avance)
                
                if tortuga.position()[0] >= self.__finishline:
                    hayGanador = True
                    print("La tortuga de color {} ha ganado".format(tortuga.color()[0]))
                    break
                
    
    
if __name__ == '__main__':
    circuito = Circuito(640, 480)
    circuito.participan('Yohana', 'Sara', 'Gerardo')
    circuito.competir()
    
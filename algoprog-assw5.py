class Circle:
    def __init__(self,radius,color):
        self.radius = radius
        self.color = color
        self.pi = 3.14
    def getColor(self):
        return self.color
    
    def getCircum(self):
        return 2*self.pi*self.radius
    
def round():
    radius = float(input("Enter a number for the radius : "))
    color = input("Enter a color for the circle : ").upper()
    if color == "RED" : 
        print("The color of the circle is now red!")
    elif color == "BLUE" :
        print("The color of the circle is now blue!")
    elif color == "GREEN" : 
        print("The color of the circle is now green!")
    else : 
        print("Im sorry there's only 3 colors :(")

    round = Circle(radius, color)

    
    print(f"Circumference : {round.getCircum()}")
    print(f"Color : {round.getColor()}")

if __name__ == '__main__' : 
    round()

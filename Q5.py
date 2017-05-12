class Rectangle:

    def __init__(self, userinput):
        if len(userinput) > 2:
            x = userinput
            self.width = abs(float(x[1]) - float(x[3]))
            self.height = abs(float(x[0]) - float(x[2]))
        else:
            y = userinput
            self.width = abs(float(y[0]))
            self.height = abs(float(y[1]))

    def calculatearea(self):
        """calculates the area of the rectangle"""
        return self.width * self.height

    def calculateperimeter(self):
        """calculates the perimeter of the rectangle"""
        return (self.width * 2) + (self.height * 2)

    def issquare(self):
        """returns True is rectangle is a square"""
        if self.width == self.height:
            return True
        else:
            return False

if __name__ == "__main__":
    while True:
        userinput = tuple(input("\tTop left and bottom right coordinates (Ex. 2.9,6,6.6,2 OR\n\t"
                                "Horizontal side and vertical side integers (Ex. 8.8,5.9): ").split(','))
        myRectangle = Rectangle(userinput)
        print("The area of your rectangle is " + str(myRectangle.calculatearea()))
        print("The perimeter of your rectangle is " + str(myRectangle.calculateperimeter()))
        print("Your rectangle is a square: " + str(myRectangle.issquare()))
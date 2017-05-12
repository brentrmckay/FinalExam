import math


class Circle:
    def desccircle(self, radius):
        """desc circle will take in a radius and calculate circumference, diameter and area"""
        print("Circumference is : " + str(2 * math.pi * radius))
        print("Diameter is : " + str(2 * radius))
        print("Area is : " + str(math.pi * radius**2))


if __name__ == "__main__":
    myCircle = Circle()
    myCircle.desccircle(int(input("What is the radius of your circle? ")))


from random import randint


class Multiply:
    def __init__(self):
        """upon object creation, create two random ints between 0 - 10"""
        self.num1 = randint(0, 10)
        self.num2 = randint(0, 10)

    def verify(self, answer):
        """verify the product of random numbers is the provided answer"""
        if answer == str(self.num1 * self.num2):
            print("Correct")
        else:
            print("Incorrect")

if __name__ == "__main__":
    while True:
        problem1 = Multiply()
        answer = input("What is " + str(problem1.num1) + " * " + str(problem1.num2) + "? break to exit")
        if answer.lower() == "break":
            break
        else:
            problem1.verify(answer)
import random


class List50:
    def __init__(self):
        """upon initialization generate a list of 50 ints"""
        self.data = [random.randint(1, 25) for x in range(1, 50)]

    def checkduplicants(self):
        """iterate through the list and compare to the current item to the previous"""
        x = self.data
        last = 0
        for a in x:
            if last > 0:
                if a == last:
                    print(last, a, True)
                else:
                    print(last, a, False)
            last = a

if __name__ == "__main__":
    myList = List50()
    print("This is my tuple: %s" % myList.data)
    myList.checkduplicants()

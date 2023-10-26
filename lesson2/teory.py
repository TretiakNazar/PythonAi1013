#class Student:
#    print("Hi")
#    def __init__(self):
#        self.height = 160
#        self.money = 2000
#        print("I am alive")


#stepan = Student()
#print(stepan.height)
#print(stepan.money)
#stepan.money -= 500
#print(stepan.money)
# class Student:
#     print("Hi")
#     def __init__(self,height = 160):
#         self.height = height
#         self.money = 2000
#         print("I am alive")
#
#
# stepan = Student(height = 180)
# print(stepan.height)
# print(stepan.money)
# stepan.money -= 500
# print(stepan.money)
# class Student:
#     print("Hi")
#     amount_of_studens = 0
#
#     def __init__(self,height = 160):
#         self.height = height
#         Student.amount_of_studens += 1
#
#
#
# stepan = Student(height = 180)
# print("stepan",stepan.height,stepan.amount_of_studens)
#
# katrin = Student(height=170)
# print("katrin",katrin.height,katrin.amount_of_studens)
#
# oleg = Student()
# print("oleg",oleg.height,oleg.amount_of_studens)
class Student:
    print("Hi")
    amount_of_studens = 0

    def __init__(self,height = 160):
        self.height = height
        self.money = 2000
        Student.amount_of_studens += 1
    def printHeight(self):
        print(self.height)
    def subMoney(self,countMoney = 0):
        self.money -= countMoney
        Student.printCountMoney(self)
    def printCountMoney(self):
        print(self.money)




stepan = Student(height = 180)
stepan.printHeight()
stepan.printCountMoney()
print("-"*20)

katrin = Student(height=170)
katrin.printCountMoney()
katrin.subMoney(200)
katrin.printCountMoney()

print("-"*20)

oleg = Student()
oleg.subMoney()


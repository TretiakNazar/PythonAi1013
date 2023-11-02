class GrandParent:
    def about(self):
        print("I am GrandParent")
    def about_myself(self):
        print("I am GrandParent")
class Parent(GrandParent):
    def about_myself(self):
        print("I am Parent")
class Child(Parent):
    def __init__(self):
        super().about()
        super().about_myself()
kate = Child()


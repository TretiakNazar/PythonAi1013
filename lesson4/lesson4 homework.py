class GrandParent:
    eye_colour = "голубий"
    height = 185
    mass = 80

class Parent(GrandParent):
    height = 183
    mass = 74

class Child(Parent):
    height = 158
    mass = 40

print("GrandParent:")
print(f"Висота: {GrandParent.height}см")
print(f"Вага: {GrandParent.mass}кг")
print(f"Колір очей: {GrandParent.eye_colour}")
print("-"*20)

print("Parent:")
print(f"Висота: {Parent.height}см")
print(f"Вага: {Parent.mass}кг")
print(f"Колір очей: {Parent.eye_colour}")
print("-"*20)

print("Child:")
print(f"Висота: {Child.height}см")
print(f"Вага: {Child.mass}кг")
print(f"Колір очей: {Child.eye_colour}")
print("-"*20)

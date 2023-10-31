class Домашнітварини:
    def __init__(self, mass, height=25):
        self.height = height
        self.mass = mass

    def eat(self, addmass):
        self.mass += addmass

    def go_to_wc(self, removemass):
        self.mass -= removemass

Котик = Домашнітварини(4, 32)

print(f"Висота кота: {Котик.height} см")
print(f"Маса кота: {Котик.mass} кг")

Котик.eat(0.4)
print(f"Маса котика після того як поїв: {Котик.mass} кг")

Котик.go_to_wc(0.2)
print(f"Маса котика після того як сходив в туалет: {Котик.mass} кг")
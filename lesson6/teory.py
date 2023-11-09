from colorama import Fore, Back, Style
try:
    #a = 5 / 0
    #int("hello")
    a = int(input("Введіть ваш рахунок"))
except ZeroDivisionError:
    print(Fore.RED + "Помилка ділення на 0")
except ValueError:
    print(Fore.RED + "Помилка значення")
except :
    print("Помилка")
else:
    print(a ** 2)
finally:
    print(Fore.GREEN+"Кінець відловлее")



print(Style.RESET_ALL+"Кінець програми")
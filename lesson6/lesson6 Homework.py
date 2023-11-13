result = []

def divider(a, b):
    try:
        if a < b:
            raise ValueError("a має бути більше або однакове за b")
        if b > 100:
            raise IndexError("b має бути менше або однакове за 100")
        return a / b
    except ValueError as ve:
        print(f"Помилка значення (ValueError): {ve}")
    except IndexError as ie:
        print(f"Помилка індексу (IndexError): {ie}")
    except Exception as e:
        print(f"Помилка: {e}")

data = {10: 2, 2: 5, "123": 4, 18: 0, "132": 15, 8: 4}

for key in data:
    res = divider(key, data[key])
    result.append(res)

print(result)
import time

def vumiruvania_chasu(func, *args, **kwargs):
    start_time = time.time()
    result = func(*args, **kwargs)
    elapsed_time = time.time() - start_time
    return result, elapsed_time
def dodacania_chisel(a, b):
    return a + b
result, elapsed_time = vumiruvania_chasu(dodacania_chisel, 3, 4)
print("Результат:", result)
print("Час виконання:", elapsed_time, "секунд")
if result == 7 and 0.0 <= elapsed_time < 1.0:
    print("Ви пройшли тест!")
else:
    print("Ви не пройшли тест.")
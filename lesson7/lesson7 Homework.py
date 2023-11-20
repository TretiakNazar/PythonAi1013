def raise_to_the_degrees(number, max_degree):
    n = 0
    for _ in range(max_degree):
        yield number * n
        n += 1
res = raise_to_the_degrees(2, 250)
print(res)
for _ in res:
    print(_)
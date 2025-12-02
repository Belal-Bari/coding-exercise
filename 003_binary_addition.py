def add_binary(a,b):
    num = a + b
    quo = ''
    while num != 0:
        quo = f'{num % 2}' + quo
        num = num // 2
    return quo

print(add_binary(0, 278))

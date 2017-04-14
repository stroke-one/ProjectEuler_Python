def fib(max_val):
    a, b  = 1, 1
    while b < max_val:
        yield b
        a, b = b, a+b

print(sum([n for n in fib(4000000) if n%2 == 0]))

## works

test = ""
a, b = 1, 1
index = 2
while len(test) < 1000:
    index += 1
    a, b = b, b + a
    test = str(b)
print(b, index)
    
    

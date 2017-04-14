
def is_five(n):
    test = str(n)
    if sum([int(digit)**5 for digit in test]) == n:
        return(n)

print(sum([x for x in range(2, 200000) if is_five(x)]))

#works

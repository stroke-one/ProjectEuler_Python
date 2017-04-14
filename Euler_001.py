def m35(n):
    if n % 3 == 0:
        return(n)
    if n % 5 == 0:
        return(n)
    return(0)

total = [m35(n) for n in range(1, 1000)]
print(sum(total))

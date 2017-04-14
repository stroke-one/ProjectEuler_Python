
def is_pal(v):
    v = str(v)
    if v == v[::-1]:
        return(True)
    return(False)

current = 0
for n in range(999, 0, -1):
    for y in range(999, 0, -1):
        x = n*y
        if x > current:
            if is_pal(x):
                current = x
                break
        elif is_pal(x):
            break
print(current)
            
# works

import time

t = time.time()

def perms(vals):
    if len(vals) == 1:
        return([vals])
    ret = []

    for v in vals:
        permutations = perms(vals.replace(v, ""))
        for p in permutations:
            ret.append(v + p)
    return(ret)

n = "0123456789"

x = (perms(n))
print(x[999999])

print(time.time() - t)

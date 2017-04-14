
def name_val(n):
    return(sum([ord(letter)-64 for letter in n]))

all_names = open("./Euler_022_names.txt", 'r').read().split(",")
all_names = sorted([name.strip('"') for name in all_names])

running_total = 0
position = 1
while all_names:
    running_total += position * name_val(all_names.pop(0))
    position += 1
print(running_total)
    

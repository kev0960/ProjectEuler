num = 1
for i in range(1, 101):
    num *= i
    
num = list(str(num))
total = 0
for i in num:
    total += int(i)
print(total)

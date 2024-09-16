"""Factorial Calculation"""
print()
number = int(input('3nt3r a Magic Numb3r to Know Th3 Factorial: '))

a = []

for i in range(1, number + 1):
    a.append(i)
   
res = 1

for factorial in a:
    res *= factorial

print(res)





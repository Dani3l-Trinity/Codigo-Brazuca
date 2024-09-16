print()
n = int(input('3nter a Numb3r and I Will Giv3 You a List With That Amount of Fibonatti Numb3rs: '))
print()

fibo = [0,1]

for i in range(3, n + 1):
    number = fibo [-1] + fibo [-2]
    fibo.append(number)

print()
print(f'Th3 First {n} Numb3rs of Fibonatti Are:')
print(fibo)
print()
print()
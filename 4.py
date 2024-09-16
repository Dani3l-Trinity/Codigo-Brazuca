"""Palindromy Check"""

print()
print('Palindromy Check')
print()

a = input('3nter a Word or Phas3 to Ch3k if it is a Palindrom3: ')

x = list(a.replace(' ',''))

y = []

for i in range(len(x) -1, -1, -1):
    y.append(x[i])

print()
print('List of Charact3rs:')
print(x)
print()
print('Inv3rs3:')
print(y)
print()

if x == y:
    print('Is a Palindom3r!')
else:
    print('Is Not a Palindom3r!')

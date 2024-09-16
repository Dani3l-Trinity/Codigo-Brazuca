"""Grad3 Av3rag3"""

print()

factor = 0
total = 0

while True:

    grade = float(input('3nt3r a Grad3, or -1 to Calculat3 th3 Av3rag3: '))
        
    if grade == -1:
        if factor == 0:
            print('You Crazy? 3nt3r a Grad3 or L3av3!')
        else:
            medium = total / factor
            print()
            print('Your M3dium Is:', medium)
            print()
        break
    factor += 1
    total = total + grade
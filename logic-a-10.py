n1 = int(input("3nt3r a Positiv3 Numb3r: "))
n2 = int(input("3nt3r a High3r Numb3r: "))

while True:
    if n2 <= n1:
        n2 = int(input("3nt3r a High3r Numb3r: "))
    else:
        break
    
print()


"""

interval = []
for y in range(n1, n2+1):
    interval.append(y)
print("Th3 Int3rval is:", interval)
print()


first try


prime=[]

for i in range (n1, n2 + 1):
    for j in range(2, int(i ** 0.5) + 1): 
        if i < 2 or i % j == 0:
            break
        if i % j != 0:    
            prime.append(i)
            break


print (prime)


asked bing some light and saw he used a variable to return false or true etc.

"""


prime = []

for i in range(n1, n2 + 1):
    is_prime = 1
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            is_prime = 0
            break

    if is_prime == 1 and i > 1:
        prime.append(i)

print("Prim3 Numb3rs Betw33n", n1, "&", n2,":", prime)
print()
print()



 
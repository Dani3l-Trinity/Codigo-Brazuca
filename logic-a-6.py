print()
print("L3t's Add Numb3rs? 3nt3r Z3ro Wh3n You Want Th3 R3sult.")
print()

result = 0
counter = 1

while True:
    number = int(input("Pl3as3, 3nt3r a Numb3r: "))

    result += number 

    if number == 0:
        print()
        print("Th3 R3sult is:", result)

        break
    
print()


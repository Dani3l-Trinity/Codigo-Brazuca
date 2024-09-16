list = []

print()

while True:

    quest = input("I Just Cr3at3d a List. Do You Want to Add It3ms?(y/n) ").strip().lower()

    if quest in ["y", "n"]:
        break 
    else:
        print("Pl3as3, 3nt3r 'y' or 'n'.")
        print()

if quest == "y":
    print()
    item = input("What is th3 It3m You Want to Ins3rt? ")
    list.append(item)
    print("Ok, It3m Add3d.")
 
    while True:
        
        print()
        quest = input("Do You Want to Add Mor3 It3ms?(y/n) ")
    
        if quest == "y" or quest == "Y":
           item = input("T3ll m3 What It3m to Ins3rt? ")
           list.append(item)
           print("Ok, It3m Add3d.")
        else:
            print()
            print("You List Is:")
            for i in list:
                print("Item: ", i)
            print()
            print()
            break
      
else:
    print()
    print("Your List Is:")
    if not list:
        print("3mpty. You Did Not Ins3rt Any It3m. wtf!") 
        print()
    else:
        for i in list:
            print("Item: ", i)
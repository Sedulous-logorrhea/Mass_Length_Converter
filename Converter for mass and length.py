import length as l
import mass as m
import time

choice = 0
ch='y'
while ch in "yY":
    print("\n............MENU...........")
    print("1. Length")
    print("2. Mass")
    print("3. QUIT\n")

    choice=int(input("Enter your choice:"))

    if (choice==1):
        print("\n............MENU For LENGTH...........")
        print("1. mile to km")
        print("2. Km to mile")
        print("3. Feet to inches")
        print("4. Inches to feet")
        print("5. QUIT\n")

        choice1 = int(input("Enter your choice:"))

        if (choice1 == 1):
            print("\n ============= mile to km ===========")
            length = int(input("In mile :"))
            print("Km         :", l.miletokm(length))

        elif (choice1 == 2):
            print("\n ============= Km to mile ===========")
            length = int(input("In Km :"))
            print("Mile         :", l.Kmtomile(length))

        elif (choice1 == 3):
            print("\n ============= Feet to inches ===========")
            length = int(input("In Feet :"))
            print("Inches         :", l.Feettoinches(length))

        elif (choice1 == 4):
            print("\n ============= Inches to feet ===========")
            length = int(input("In Inches :"))
            print("Feet         :", l.Inchestofeet(length))

        elif (choice1 == 5):
            print("\n ============= Ending the program in...")
            print("3")
            time.sleep(0.5)
            print("2")
            time.sleep(0.5)
            print("1")
            time.sleep(0.5)

        else:
            print("Invalid Entry.")
    if (choice == 2):
        print("\n............MENU For MASS...........")
        print("1. Kg to tonne")
        print("2. Km to mile")
        print("3. Feet to inches")
        print("4. Inches to feet")
        print("5. QUIT\n")

        choice2 = int(input("Enter your choice:"))

        if (choice2 == 1):
            print("\n ============= Kg to tonne ===========")
            mass = int(input("In Kg :"))
            print("Tonne         :", m.Kgtotonne(mass))

        elif (choice2 == 2):
            print("\n ============= Tonne to kg ===========")
            Mass = int(input("In Tonne :"))
            print("Kg         :", m.Tonnetokg(Mass))

        elif (choice2 == 3):
            print("\n ============= Kg to pound ===========")
            Mass = int(input("In Kg :"))
            print("Pound         :", m.Kgtopound(Mass))

        elif (choice2 == 4):
            print("\n ============= Pound to kg ===========")
            Mass = int(input("In Pound :"))
            print("Kg         :", m.Poundtokg(Mass))

        elif (choice2 == 5):
            print("\n ============= Ending the program in...")
            print("3")
            time.sleep(0.5)
            print("2")
            time.sleep(0.5)
            print("1")
            time.sleep(0.5)

        else:
            print("Invalid Entry.")
    ch = input("Do you want to continue(Y/N)? :")
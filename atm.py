pin = "1234"
incrementer = 0

for i in range(3):
    inputPin = input("Please enter your pin: ")
    if incrementer != 3:
        if(inputPin == pin):
            print(" 1. Cash deposit \n 2. Cash withdrawal \n 3. Exit\n")
            option = input("Enter your option:")
            if(option == "1"):
                print("Please insert the cash...")
            elif(option == "2"):
                print(" 1. 500\n 2. 1000\n 3. 5000")
                cashWithdrawal = input("Please select the amount:")
                if(option == "1" or "2" or "3"):
                    print("Cash being withdrawed, please wait...")
            elif(option == "3"):
                print("Card is being removed, please be patient.")
        else:
            print("Please try again.")
            incrementer += 1
            if incrementer == 3:
                print("Your account has been locked.")
      




    

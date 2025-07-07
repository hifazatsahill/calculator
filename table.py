while True:# ya program ko coninuse chlany k liya use hota ha
    # yahan pa user ko Menu show krty hain
    print("Menu:")
    print("1. Generate Table")
    print("2. Exit")
    
    choice = input("Enter your choice (1 or 2): ") # ya user ko show krty ki ki in number ma ce koy ak enter kray

    if choice == "1":
        # Table Generator
        user_input = input("Enter a number to generate its table: ")
        try: # ya to check krey ga user ka input kai ha usky mutabiq run kreey gaa
            num = int(user_input)
        except ValueError:
            print("Please enter a valid integer.\n")
            continue

        print(f"\nMultiplication Table of {num}:")
        for i in range(1, 11):# yahan par for loop chlaa rhy hain 1,10 tak aur her number i k liya table genrate krta ha
            print(f"{num} x {i} = {num * i}")
        
    elif choice == "2":
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1 or 2.\n")

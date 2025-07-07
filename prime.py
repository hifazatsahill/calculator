# prime number checker project

def is_prime(n):
    if n <= 1:
        return False
    # ya value ko check kreegaa ka input prime ha ki nae

    for i in range(2, int(n**0.5) + 1): # ab yahaan pa for loop ka use kiya ha ya check krnay ka liya ki squre root leny ce ksi output data ya check kree gaa
        if n % i == 0:# agr n ko i ki koy value divide kray aur answer 0 aye wo prime nae ha false hogaa

            return False
    return True 

while True:# ya bar bar jo value chalani hoti ha usky liya while loop ka istimal kiya jataa ha
    user_input = input("Enter Your Value ")
    if user_input.lower() == "exit":# agr user exit likh kr enter krey ga to programe break hojyie gaa

        print("Exiting your program because you input 'exit'.")
        break
    try:#ys User ki input value check krny k liy use kiya jataa ha
        num = int(user_input)
    except ValueError: # agr user intiger ka alawah koy aur data to value error show kreey gaa
        print("Please enter a valid integer.")
        continue # ya loop ko continue rakhtaa ha ager user ka input correct ho to

    if is_prime(num): # ya number check krny ka baad print value dega ki number prime ha ya nae
        print(f"{num} is a prime number.\n")
    else:
        print(f"{num} is not a prime number.\n")
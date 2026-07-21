attempt = 0 #it's an counter variable 
while attempt <3:
    password =int(input("Enter Your Password ")) # We need the input for pin so we can define is it wrong or what 
    if password == 6969 :
        print(f"Login Succesful")
        break
    else:
        print(f"your reamaining attempt is {3- attempt }")
        attempt +=1
if attempt==3:
    print("Your All Sessions are finished ,Try Again Later !")
attempt = 0
while attempt <3:
    password =int(input("Enter Your Password "))
    if password == 6969 :
        print(f"Login Succesfull")
        break
    else:
        attempt +=1
        print(f"your reamaining attempt is {3- attempt }")

#ask username, password
# if username, password correct - print Welcome

#if username or password or both incorrect, ask again, print:Incorrect
#until 5 times - Access denied
# inside loop check again if correct, break loop, print Welcome

#attempts here = 1 as ask username, password right at the beginning (counted as 1st time)


username = input("Enter username: ")
password = input("Enter password: ")

attempts = 1

if username == 'python' and password == 'rules':
    print ("Welcome")

else:
    while attempts < 5:
        print("Incorrect username or password. Please try again.")
        username = input("Enter username: ")
        password = input("Enter password: ")
        attempts += 1
        if username == 'python' and password == 'rules':
            print ("Welcome")
            break  
    else: 
        print("Access denied")    

    
       
    


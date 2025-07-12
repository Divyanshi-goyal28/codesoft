import string
import random

# Getting password length
password_length = int(input("Enter password length: "))

print('''Choose character set for password from these : 
         1. Digits
         2. Letters
         3. Special characters
         4. Exit''')

characterList = ""

# Getting character set for password
while(True):
    choice = int(input("Choose an option(1-4): "))
    if(choice == 1):
        
        # Adding letters to possible characters
        characterList += string.ascii_letters
    elif(choice == 2):
        
        # Adding digits to possible characters
        characterList += string.digits
    elif(choice == 3):
        
        
        characterList += string.punctuation
    elif(choice == 4):
        break
    else:
        print("Please pick a valid option!")

password = []

for i in range(password_length):
  
    
    selected_char = random.choice(characterList)
    
   
    password.append(selected_char)

# printing password as a string
print("The generated password is " + "".join(password))
import sys      #to access command line args through the terminal
import adduser, deluser,passwd,login        #importing modules that we created for user management system

cmd_line_argument= sys.argv[1]      #assigning cmd_line_argument with sys arguments that takes python and text file

try:
    while True:
        user_choice= None       #we never know when or what will user enter so a none value works only when necessary
        
        user_choice= input("User@Management_System: ")      #asking for user entry 
        
        if user_choice == "adduser":            #if user entry is adduser it takes the code to adduser.py file inside its main function
            adduser.main(cmd_line_argument)
        
        elif user_choice == "deluser":           #if user entry is deluser it takes the code to deluser.py file inside its main function
            deluser.main(cmd_line_argument)
            
        elif user_choice == "changepw":          #if user entry is changepw it takes the code to passwd.py file inside its main function
            passwd.main(cmd_line_argument)
        
        elif user_choice == "login":             #if user entry is login it takes the code login.py file inside its main function
            login.main(cmd_line_argument)
            
        elif user_choice=="passwd.txt":
            with open(cmd_line_argument,"r") as file:
                content=file.read()
                print("Contents of file passwd.txt:\n")
                print(content)
        
        elif user_choice == "help":              #if user enter help it will display the functions of the system and the keywords necessary for it to be activated
            print("'passwd.txt': shows content of passwd file".rjust(43))
            print(" 'adduser': adds user ")
            print(" 'deluser': deletes user ")
            print(" 'changepw': changes password ")
            print(" 'login': log in into the user ")
            print("'exit' exit the commandlines".rjust(29))
            
        elif user_choice == "exit":             #if user enter exit the code will break out of loop and exits itself
            break
            
        else:                                   #if neither of the entry matches with the above commands then Invalid command
            print(f"\nInvalid command! {user_choice} \nPlease type 'help' to see list of commands")
            
except FileNotFoundError:                       #if wrong file entry then file not found error
    print("\nFile not found!\n  try again")
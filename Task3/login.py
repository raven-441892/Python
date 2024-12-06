import sys      #to access command line args through the terminal
import codecs       #to access rot 13 encryption from this module
import getpass      #this module takes password in hidden form

def main (cmd_line_argument):       #accessing and sending cmd_line_argument from and to task 3 
    
    def login_user(username, password):
        try:
            # reads the content of passwd.txt file
            with open (cmd_line_argument,"r") as file :
                lines = file.readlines()

            # creates two list one for username and other for passwords and adds all the username and passwords of the txt file into the respective lists
            existing_usernames = []
            existing_passwords=[]
            for line in lines:
                piece= line.split(':')
                existing_usernames.append(piece[0])
                existing_passwords.append(piece[2].strip())     #strip now removes the excess white spaces line new line
            
            #checks if the user entered username is in existing_usernames list if so the code continues inside the condition block
            if username in existing_usernames:
                
                #now the user entered password get encrypted with rot_13
                password=codecs.encode(password, 'rot_13')
                
                #if the encrypted password matches within the existing_passwords list then the access is granted
                if password in existing_passwords:
                    print("Access granted")

                #or else the access is denied
                else:
                    print("Access denied")
            
            #if user entered username not found in existing_usernames then else condition runs
            else:
                print(f"'{username}' username does not exist. Access denied")
        
        #exception when file is not found      
        except FileNotFoundError:
            print("File not found!")

    #ask user for username to login
    user = input("User: ")
        
    #ask user the password of that username in hidden format
    password = getpass.getpass("Enter password: ")
        
    #function call
    z=login_user(user,password)



        

                
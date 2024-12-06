import sys      #to access command line args through the terminal
import codecs       #to access rot 13 encryption from this module
import getpass      #this module takes password in hidden form

def main (cmd_line_argument):   #accessing and sending cmd_line_argument from and to task 3
    
    def del_user(username,password):
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
                
                #if the encrypted password matches within the existing_passwords list then the code continues
                if password in existing_passwords:
                    
                    #now new_lines list is created which stores the lines in which the user name entered by user is not match
                    new_lines=[]
                    for line in lines:
                        if line.split(':')[0] != username:
                            new_lines.append(line)
                    
                    #writes back to the passwd.txt file without the deleted account details
                    with open (sys.argv[1],"w") as file:
                        file.writelines(new_lines)
                    
                    print(f"User '{username}' deleted")
                    
            #else condition for when username is not found in exisitng_usernames list       
            else:
                print("Nothing has changed")
                
        #exception when file is not found        
        except FileNotFoundError:
            print("File not found!")

    #asks user for the user name that is to be deleted 
    del_username = input("Enter username: ")
        
    #asks user for the password of the user to be deleted
    enter_password=getpass.getpass("Enter password: ")
        
    #funstion call
    z=del_user(del_username,enter_password)



        

                
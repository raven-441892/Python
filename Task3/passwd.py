import sys      #to access command line args through the terminal
import codecs       #to access rot 13 encryption from this module
import getpass      #this module takes password in hidden form

def main (cmd_line_argument):   #accessing and sending cmd_line_argument from and to task 3
    
    def change_pass(username, cur_password, ne_password, con_password):
        try:
            # reads the content of passwd.txt file
            with open (cmd_line_argument,"r") as file :
                lines = file.readlines()

            # creates two list one for username and other for new lines which consist of new lines with password changed 
            existing_usernames = []
            new_lines=[]

            #for loop runs line by line of the file
            for line in lines:
                #splits the words of a line with a colon and assign it to the piece list
                piece= line.split(':')
                
                #puts the first element of piece in existing_usernames list
                existing_usernames.append(piece[0])
                
                #now if the first element of piece matches the username
                if piece[0]==username:
                    #encrypted current password is stored in that variable
                    cur_password_encrypted=codecs.encode(cur_password,'rot_13')
                    
                    #if the encrypted current password matches the third element of piece then the condition continues
                    if piece[2].strip()==cur_password_encrypted:
                        #encrypted new password is stored in that variable
                        ne_password_encrypted=codecs.encode(ne_password,'rot_13')
                        
                        #third element of piece is replaced by encrypted new password 
                        piece[2]=f"{ne_password_encrypted}\n"
                        
                        #now new element of piece is joined with :
                        line=':'.join(piece)
                        
                #changed password lines are added into new_lines list  
                new_lines.append(line)

            #condition when the username is not found
            if username not in existing_usernames:
                print("User dont exist")
                return
            
            #writes the new_lines in the file    
            with open (sys.argv[1],"w") as file:
                    file.writelines(new_lines)
            print(f"Password changed of username {username}")
        
        #exception when file is not found                 
        except FileNotFoundError:
            print("File not found!")
        
    #asks user for the username of whose password is to be changed
    just_username = input("User: ")
        
    #asks user for the current password of that username
    current_pass = getpass.getpass("Current password: ")
        
    #asks user for the new password of that username
    new_password=getpass.getpass("New password: ")
        
    #asks user for the password of that username for confirmation
    confirm_pass=getpass.getpass("Confirm password: ")
        
    #condition that checks if the new password matches the confirm password or not
    if new_password!=confirm_pass:
        print("Error: New password and confirm password don't match.")
        
    else:
        #function call
        change_pass(just_username, current_pass, new_password, confirm_pass)



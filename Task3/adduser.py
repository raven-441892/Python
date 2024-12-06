import sys          #to access command line args through the terminal
import codecs       #to access rot 13 encryption from this module

def main(cmd_line_argument):    #accessing and sending cmd_line_argument from and to task 3
    
    def add_user(username, real_name, password):
        try:
            #reads the content of passwd.txt file
            with open (cmd_line_argument,"r") as file :
                lines = file.readlines()

            # creates a list and adds all the username of the txt file into the list
            existing_usernames = []
            for line in lines:
                user= line.split(':')[0]        #each word from a line gets split by : and then takes the first element
                existing_usernames.append(user)     #adds the user to that list
        
            #checks if the entered username already exists in that list or not
            if username in existing_usernames:
                print("Error: Username already exists.")
                return      #exits from the function directly and doesnt continue the function further or else even if error occurs it will create the user

            #checks if the user entered username is not in lowercase then it gives back an error
            if username!=username.lower():
                print("Error : Enter username in lowercase")
                
            # checks the user entered name is lowercase then add the new user entry
            if username==username.lower():
                new_entry = f"{username}:{real_name}:{password}\n"      #puts the new entry in a certain format
                lines.append(new_entry)

                # writes the updated content back to passwd.txt file
                with open (sys.argv[1],"w") as file:
                    file.writelines(lines)      #it writes list of strings whereas write only accepts a string
                    
                #notifies that the new user is created    
                print(f"User '{username}' created")
        
        #if file not found then this work as error handling  
        except FileNotFoundError:
            print("File not found!")

        #asks user for their username
    new_username = input("Enter new username: ")
        
        #asks user for their name
    new_real_name = input("Enter real name: ")
        
        #asks user for their password
    new_password=input("Enter password: ")
        
        #the entered password is then encrypted with ROT_13 encryption
    new_password=codecs.encode(new_password,"ROT_13")
        
        #function call
    z=add_user(new_username, new_real_name, new_password)



        

                
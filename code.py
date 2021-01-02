import os
import pyAesCrypt
import getpass


script_loc = os.path.realpath(__file__)
print("")
input_file = input("=> Please provide the global location of the file/folder you want to process : ")
print("")
input_operation = input("=> What action do you want to take? Press E to encrypt or D to decrypt : ").lower()[0] #Dealing with case sensitive inputs or the situation when the user types the whole spelling
print("")
input_password = getpass.getpass("=> Please enter the password you want to use : ")
buffsize = 64 * 1024

def folder_action(folder_loc): #function to deal with folders
    folder_content = os.listdir(folder_loc)
    if len(folder_content) > 0: #check if the folder is empty or not
        for i in folder_content:
            present_file = os.path.join(folder_loc, i) #obtaining the global location the contents of the folder
            if os.path.isdir(present_file): #check if the encountered element is a folder
                folder_action(present_file)
            elif os.path.isfile(present_file) and present_file != script_loc: #check if the encountered element is a file and whether the file we are trying to deal with is our encryption script
                if input_operation == "e": #encrypting the file
                    pyAesCrypt.encryptFile(present_file, present_file + ".aes", input_password, buffsize)
                    os.remove(present_file)
                elif input_operation == "d": #decryypting the file
                    try:
                        pyAesCrypt.decryptFile(present_file, present_file[:-4], input_password, buffsize)
                        os.remove(present_file)
                    except: #exception handling when user entered the wrong password
                        print("=> PLEASE ENTER THE CORRECT PASSWORD")

if os.path.isfile(input_file) and present_file != script_loc: #dealing directly with a file
    if input_operation == "e":
        pyAesCrypt.encryptFile(input_file, input_file + ".aes", input_password, buffsize)
        os.remove(input_file)
    elif input_operation == "d":
        try:
            pyAesCrypt.decryptFile(input_file, input_file[:-4], input_password, buffsize)
            os.remove(input_file)
        except:
            print("=> PLEASE ENTER THE CORRECT PASSWORD")

elif os.path.isdir(input_file): #dealing with a folder
    folder_action(input_file)
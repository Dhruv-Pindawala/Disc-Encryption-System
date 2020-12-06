import magic
import os
import pyAesCrypt
import getpass

file_input = input("=> Please enter the GLOBAL LOCATION of the file : ")
file_type = "None"


try:
    if os.path.isfile(file_input):
        file_type_initial = magic.from_file(file_input, mime = True)
        file_type = file_type_initial[1 + file_type_initial.rfind('/'):]
        print("=> We are dealing with a {} file.....".format(file_type.upper()))
    elif os.path.isdir(file_input):
        file_type = "directory"
        print("=> We are dealing with a DIRECTORY.....")
    action = input('=> what action do you want to take? Press E to encrypt or D to decrypt : ').lower()
    password = getpass.getpass("=> Please enter the PASSWORD : ")
    buffersize = 64 * 1024

except:
    print("=> Please enter a valid file location.")



def file__action(file1, action1, password1, buffersize1):
    if action == action1 and file_type != "None" and file_type != 'directory':
        pyAesCrypt.encryptFile(file1, file1+".aes", password1, buffersize1)
        os.remove(file_input)
    elif action == action1 and file_type != "None" and file_type != 'directory':
        pyAesCrypt.decryptFile(file1, file1[:-4], password1, buffersize1)
        os.remove(file_input)
try:
    if os.path.isfile(file_input):
        file__action(file_input, action, password, buffersize)

except:
    print("=> Sorry for the inconvenience faced. We are unable to process your input.......")
    print("=> please create a new issue in the repository and we will try to sort it as soon as possible!!!!!!!")
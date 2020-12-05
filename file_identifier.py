import magic
import os
import pyAesCrypt

file_input = input("=> Please enter the GLOBAL LOCATION of the file : ")
file_type = "None"


try:
    if os.path.isfile(file_input):
        file_type_initial = magic.from_file(file_input, mime = True)
        file_type = file_type_initial[1+file_type_initial.rfind('/'):]
        print("=> The file format of the given file is {}.....".format(file_type.upper()))
    elif os.path.isdir(file_input):
        file_type = "directory"
        print("=> We are dealing with a DIRECTORY.....")

except:
    print("=> Please enter a valid file location.")

action = input('=> what action do you want to take? Press E to encrypt or D to decrypt : ').lower()
password = input("=> Please enter the PASSWORD : ")
buffersize = 64 * 1024

if action == 'e' and file_type != "None" and file_type != 'directory':
    pyAesCrypt.encryptFile(file_input, file_input+".aes", password, buffersize)
elif action == 'd' and file_type != "None" and file_type != 'directory':
    pyAesCrypt.decryptFile(file_input, file_input[:-4], password, buffersize)
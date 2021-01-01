import os
import pyAesCrypt
import getpass

print("")
input_file = input("=> Please provide the global location of the file/folder you want to process : ")
print("")
input_operation = input("=> What action do you want to take? Press E to encrypt or D to decrypt : ").lower()[0]
print("")
input_password = getpass.getpass("=> Please enter the password you want to use : ")
buffsize = 64 * 1024

if os.path.isfile(input_file):
    if input_operation == "e":
        pyAesCrypt.encryptFile(input_file, input_file + ".aes", input_password, buffsize)
        os.remove(input_file)
    elif input_operation == "d":
        try:
            pyAesCrypt.decryptFile(input_file, input_file[:-4], input_password, buffsize)
            os.remove(input_file)
        except:
            print("PLEASE ENTER THE CORRECT PASSWORD")

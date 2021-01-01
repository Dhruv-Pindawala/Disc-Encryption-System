import magic
import os
import pyAesCrypt
import getpass

file_input = input("=> Please enter the GLOBAL LOCATION of the file : ")
file_type = "None"
action = input('=> What action do you want to take? Press E to encrypt or D to decrypt : ').lower()
password = getpass.getpass("=> Please enter the PASSWORD : ")
buffersize = 64 * 1024


def file_action(file1, action1, password1, buffersize1):
    if action1 == 'e' and file_type != "None":
        pyAesCrypt.encryptFile(file1, "encrypted_" + file1, password1, buffersize1)
        os.remove(file1)
    elif action1 == 'd' and file_type != "None":
        pyAesCrypt.decryptFile(file1, file1[10:], password1, buffersize1)
        os.remove(file1)

def dir_action(working_dir, action1, password1, buffersize1):
    dir_list = os.listdir(working_dir)
    print(dir_list)
    if len(dir_list) > 0:
        for new_file in dir_list:
            present_file = os.path.join(working_dir, new_file)
            print(present_file)
            if os.path.isfile(present_file):
                file_action(present_file, action1, password1, buffersize1)
            elif os.path.isdir(present_file):
                dir_action(present_file, action1, password1, buffersize1)



print("Present directory is :",os.getcwd())

if os.path.isfile(file_input):
    file_type_initial = magic.from_file(file_input, mime = True)
    file_type = file_type_initial[1 + file_type_initial.rfind('/'):]
    last_slash = file_input.rfind('\\')
    print(os.getcwd())
    print("Dhruv")
    file_action(file_input, action, password, buffersize)
elif os.path.isdir(file_input):
    file_type = "directory"
    os.chdir(file_input)
    dir_action(file_input, action, password, buffersize)


#except:
#    print("=> Please enter a valid file location.")

#except:
#    print("=> Sorry for the inconvenience faced. We are unable to process your input.......")
#   print("=> Please check if you have given all the asked inputs clearly and try to run the program once again..")
#    print("=> please create a new issue in the repository and we will try to sort it as soon as possible!!!!!!!")
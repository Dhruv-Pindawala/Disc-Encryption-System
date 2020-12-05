import magic

file_input = input("=> Please enter the GLOBAL LOCATION of the file : ")
try:
    file_type_initial = magic.from_file(file_input, mime = True)
    file_type = file_type_initial[1+file_type_initial.rfind('/'):]
    print("=> The file format of the given file is {}".format(file_type.upper()))
except:
    print("=> Please enter a valid file location.")
action = input('=> what action do you want to take? Press E to encrypt or D to decrypt')

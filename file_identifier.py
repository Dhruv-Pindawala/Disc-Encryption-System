import magic

file_input = input("Please enter the GLOBAL LOCATION of the file : ")
try:
    file_type_initial = magic.from_file(file_input, mime = True)
    file_type = file_type_initial[1+file_type_initial.rfind('/'):]
except:
    print("Please enter a valid file location.")

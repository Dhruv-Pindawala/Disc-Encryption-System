import magic

file_input = input("Please enter the GLOBAL LOCATION of the file : ")
try:
    file_type = magic.from_file(file_input, mime = True)
    print(file_type)
except:
    print("Please enter a valid file location.")

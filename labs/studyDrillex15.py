from sys import argv

script, filename = argv
#This line makes variables for when a file is supposed to be written
txt = open(filename)
#these lines takes the filename and reads it out to the user
print(f"Here's your file {filename}:")
print(txt.read())


file_again = input("> ")
#This line allows the user to type in another filename if nessecary this line dosen't need to be present for the codes operation but is usefull for jumping from file to file
txt_again = open(file_again)


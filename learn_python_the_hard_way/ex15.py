from sys import argv

script, filename = argv # get the filename from the user with keyboard

# filename = input("Please input the filename.")
txt = open(filename) # open the fiel

print(f"Here's your file {filename}:")
print(txt.read()) # use the read function to read file and output

txt.close()
# print("Type the filename again:") # get another filename
# file_again = input(">") # print the prompt symbol

# txt_again = open(file_again) # the same as line 5

# print(txt_again.read()) # the same as line 8
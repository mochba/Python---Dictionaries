#  Need more practice and ?????

# Exercise 9.4 Write a program to read through the mbox-short.txt and figure out who 
# has sent the greatest number of mail messages. The program looks for 'From ' lines 
# and takes the second word of those lines as the person who sent the mail.
# The program creates a Python dictionary that maps the sender's mail address to a 
# count of the number of times they appear in the file. After the dictionary is produced, 
# the program reads through the dictionary using a maximum loop to find the most 
# prolific committer

email_list = list()
file_name = 'mbox-short.txt'
# file_name = input("Enter the file name:")
file_handle = open(file_name)

for each_line in file_handle:
    if each_line.startswith('From '):
        line_list = each_line.split()
        email = line_list[1]
        email_list.append(email)
print(email_list)
email_dictionary = dict()
for email_1 in email_list:
    c = email_list.count(email_1)
    email_dictionary[email_1] = c
print("\n",email_dictionary)
m = email_dictionary.items()

for email,count in m:
    
print("\n", m)













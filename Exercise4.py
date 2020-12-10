"""Exercise 4: Write a program to read through a mail log, build a histogram using a 
dictionary to count how many messages have come from each email address, and print 
the dictionary. Look through the dictionary using a maximum loop 
(see Chapter 5: Maximum and minimum loops) to find who has the most messages and 
print how many messages the person has.
for the file mbox-short.txt or mbox.txt
/home/appu/Documents/python_workbench/Chuks_python/mbox-short.txt"""
email_list = list()
email_count_dict = dict()
try:
    stream = open(input("Enter a file name: "))
    for each_line in stream:
        each_line = each_line.strip()
        # print("\t\\\\\\\\",each_line)
        if each_line.startswith("From "):
            word_list = each_line.split()
            # print("\t\t++++++++++++++++++++++++++++",line_list)
            email = word_list[1]
            # print("\t\t\t=======",email)
            email_list.append(email)
    # print("Email list from the text file \n",email_list,"\n")
    for each_email in email_list:
        email_count_dict[each_email] = email_count_dict.get(each_email,0) + 1
    print("\tEmail count",email_count_dict)
    
    max_email = None
    max_emailcount = None
    for k_email,v_emailcount in email_count_dict.items():
        if max_emailcount is None or v_emailcount > max_emailcount:
            max_emailcount = v_emailcount
            max_email  = k_email
    print(max_email,max_emailcount)

except:
    print("File not found")
    quit()
"""# Exercise 3: Write a program to read through a mail log, build a histogram using a 
# dictionary to count how many messages have come from each email address, and print 
# the dictionary.For the file mbox-short.txt or mbox.txt"""
email_list = list()
email_count_dict = dict()
try:
    getfile = input("Enter a file name:")
    stream = open(getfile)
    for each_line in stream:
        each_line = each_line.strip()
        if each_line.startswith("From "):
            wordslist = each_line.split()
            # print("list of words ",wordslist)
            email = wordslist[1]
            # print(email)
            email_list.append(email)        
    print(email_list)
    for each_email in email_list:
        print(each_email)
        email_count_dict[each_email] = email_count_dict.get(each_email,0) + 1
    print(email_count_dict)
except:
    print("Enter a valid file name!!!!!!!!!!!!!!!!!!!")
    quit()
""" How to add in histogram method"""
# daylist = ['s','m','w','f','t','w','f','t','s','m','w']
# day_count_dict= dict()
# for day in daylist:
#         day_count_dict[day] = day_count_dict.get(day,0) +  1
# print("Day Count",count,"\n")   
""" How to append"""
# t = ['a', 'b', 'c']
# t.append('d')
# print(t)
# ['a', 'b', 'c', 'd']
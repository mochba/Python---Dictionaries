"""# Exercise 2: Write a program that categorizes each mail message by which day of the 
# week the commit was done. To do this look for lines that start with "From", then look 
# for the third word and keep a running count of each of the days of the week. 
# At the end of the program print out the contents of your dictionary
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"""
# /home/appu/Documents/python_workbench/Chuks_python/mbox-short.txt
day_count_dict = dict()
daylist = list()
try:
    getfile = input("\nENTER the file name: ")
    stream = open(getfile)
    for each_line in stream:
        each_line = each_line.strip()
        print(each_line)
        if each_line.startswith("From "):
            wordlist = each_line.split()
            print("wordlist",wordlist)
            day = wordlist[2]
            daylist.append(day)
            print("daylist",daylist)
        else:
            continue
    print("\ndaylist",daylist,"\n")

    for day in daylist:
        day_count_dict[day] = day_count_dict.get(day,0) +  1
    print("Day Count",day_count_dict,"\n")
    
except:
    print("\nFile  not found I am quiting")
    quit()    


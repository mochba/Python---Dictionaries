# Exercise 5: This program records the domain name (instead of the address) where the 
# message was sent from instead of who the mail came from (i.e., the whole email address).
# At the end of the program, print out the contents of your dictionary.
# for the file mbox-short.txt or mbox.txt

getfile = input("Enter file name :")
# getfile = "mbox-short.txt"
email_list = list()
name_and_domain_list = list()
domain_namelist = list()
domain_name_count = dict()

try:
    stream = open(getfile)
    for each_line in stream:
        each_line.strip
        if each_line.startswith("From "):
            wordlist_eachline = each_line.split(' ')
        # print("================",wordlist_eachline)
            email = wordlist_eachline[1]
            email_list.append(email)
            name_and_domain_list = wordlist_eachline[1].split('@')
        # print("@@@@@@@@",name_and_domain_list)
            domain_name = name_and_domain_list[1]
        # print("domain_name domain_name domain_name",domain_name)
            domain_namelist.append(domain_name)
    print("\nAll the Domain name in the text files are\n\n" , domain_namelist,"\n")

    for each_domainname in domain_namelist:
        domain_name_count[each_domainname] = domain_name_count.get(each_domainname,0) + 1
    print("Domain Name Count dictionary \n" , domain_name_count,"\n")

except:
    print("File name not found ")
    quit


    
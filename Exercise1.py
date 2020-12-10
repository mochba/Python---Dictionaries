"""# Write a program that reads the words in words.txt and stores them as keys in a 
# dictionary. It doesn't matter what the values are. Then you can use the in operator 
# as a fast way to check whether a string is in the dictionary.

/home/appu/Documents/python_workbench/Chuks_python/Word.txt"""

word_dict =dict()

file_stream = open(input("Enter a file name: "))

for each_line in file_stream:
    wordlist = each_line.split()
       
    for each_word in wordlist:
        if each_word in word_dict:
            word_dict[each_word] = True
        else:
            word_dict[each_word] = False  

print(word_dict)
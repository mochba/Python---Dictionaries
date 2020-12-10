"""We will write a Python program to read through the lines of the file, break each line
into a list of words, and then loop through each of the words in the line and count 
each word using a dictionary."""

#  /home/appu/Documents/python_workbench/Chuks_python/Dictionary_Excercise

count_dict =  dict()
file_name = "/home/appu/Documents/python_workbench/Chuks_python/Dictionary_Excercise/romeo.txt"

try:
    stream = open(file_name)
except:
    print('File cannot be opened:', file_name)
    exit()

for each_line in stream:
    words = each_line.split()
    for eachword in words:
        count_dict[eachword] = count_dict.get(eachword,0) + 1
# print(count_dict)

for k,v in count_dict.items():
    print(k,v)

counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
lst = list(counts.keys())
print("Before sorting: ",lst)
lst.sort()
print("After sorting: ",lst)
for key in lst:
    print(key, counts[key])













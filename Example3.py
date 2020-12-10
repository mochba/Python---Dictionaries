import string
# fname = "/home/appu/Documents/python_workbench/Chuks_python/Dictionary_Excercise/romeo.txt"

fname = input('Enter the file name: ')
fhand = open(fname)
# try:
    
# except:
#     print('File cannot be opened:', fname)
#     exit()

counts = dict()
for line in fhand:
    line = line.rstrip()
    l = line.maketrans('', '', string.punctuation)
    line = line.translate(l)
    line = line.lower()
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1
print(counts)

# intab = "aeiou"
# outtab = "12345"
# trantab = str.maketrans(intab, outtab)

# print(trantab)

# {97: 49, 101: 50, 105: 51, 111: 52, 117: 53}
# thats is replace a with 1 whose ASCII code is 97 for "a" and 49 for "1"
# AScii value of a = 97 e =101 i = 105 o = 111 u = 117
# ASCII value of 1=49 2=50 3=51 4=52 5=53

# str = "this is string example....wow!!!"
# print (str.translate(trantab))

# th3s 3s str3ng 2x1mpl2....w4w!!!
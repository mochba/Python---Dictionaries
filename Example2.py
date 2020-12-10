# Dictionary as a set of counters

name = "mohanabalapradeepbalakeethana"
letter_dict = dict()

for each_letter in name:
    if each_letter not in letter_dict:
        letter_dict[each_letter] = 1
    else:
        letter_dict[each_letter] = letter_dict[each_letter] + 1
print(letter_dict)

st = "Hello madam how are you madam"
letter_dict1 = dict()
for each_letter in st:
    letter_dict1[each_letter] = letter_dict1.get(each_letter,0) + 1
print(letter_dict1)

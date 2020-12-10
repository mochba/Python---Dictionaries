name_count_dict = dict()
# names = dict()
names = ['mohana','chitra','bala','mani','keerthana','pradeep','keerthana','bala']
# names = input("Get The name :")
for name in names:
    if name not in name_count_dict:
        name_count_dict[name] = 1
    else:
        name_count_dict[name] = name_count_dict[name] + 1
print(names,"\n",name_count_dict)

# count the number of time each day apper in the list with  histogram method

day_list = ['Sat', 'Fri', 'Fri', 'Fri', 'Fri', 'Fri', 'Fri', 'Fri', 'Fri', 'Fri', 'Fri', 'Fri', 'Fri', 'Fri', 'Fri', 'Fri', 'Fri', 'Fri', 'Fri', 'Fri', 'Fri', 'Thu', 'Thu', 'Thu', 'Thu', 'Thu', 'Thu']
day_dict = dict()
for each_day in day_list:
    day_dict[each_day] = day_dict.get(each_day,0) + 1
print(day_dict)

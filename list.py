my_list = list()
my_list = [10,20,30,40]
my_list[1] = 15
my_list = my_list + [50,60,70]
my_list.pop()
my_list.sort()
for index, item in enumerate(my_list):
    if item == 30:
        print(index)
import os


def cat_list_value():
    if os.path.exists("categ_list.txt"):
        f = open('categ_list.txt','r')
        for line in f:
            string = line
        elements = string.split(' ')
        f.close()
        return elements
    else:
        return []

total_dict = dict.fromkeys(cat_list_value(),0)


fin_list = []
f = open('costs_list.txt', 'r')
for line in f:
    elements = line.split(' ')
    lst = [elements[0][1:],int(elements[1])]
    fin_list.append(lst)

f.close()

for d in fin_list:
    total_dict[d[0]] = total_dict[d[0]]+d[1]

print(total_dict)

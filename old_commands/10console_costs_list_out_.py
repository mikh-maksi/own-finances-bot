f = open('costs_list.txt','r')
string = ''
for line in f:
    string = string+line
print(string)
f.close()


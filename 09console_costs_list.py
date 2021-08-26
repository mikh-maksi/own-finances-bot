string_in = input("Input command\n")
elements_in = string_in.split(' ')
f = open('categ_list.txt','r')

for line in f:
    string = line
elements = string.split(' ')
f.close()

if elements_in[0][1:] in elements:
    f = open('costs_list.txt','a')
    f.write(string_in+'\n')
    f.close()
    print("Category exists")
    print("Cost added")
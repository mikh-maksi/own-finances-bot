string_in = input("Input command\n")
f = open('categ_list.txt','r')
for line in f:
    string = line
f.close

elements_in = string_in.split(' ')
elements = string.split(' ')

print(elements_in[0][1:])
print(elements)

if elements_in[0][1:] in elements:
    print("Category exists")
    f = open('costs_list.txt','a')
    f.write(string_in+'\n')
    f.close()

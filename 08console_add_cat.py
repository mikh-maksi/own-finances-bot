string_in = input("Input command\n")
elements = string_in.split(' ')
if elements[0] == '/addcat':
    f = open('categ_list.txt','r')
    for line in f:
        string = line
    f.close
    f = open('categ_list.txt','w')
    f.write(string)
    f.write(' '+elements[1])
    f.close()
    print("Category added")
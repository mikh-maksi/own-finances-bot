# import pathlib

# path = pathlib.Path(__file__).parent.absolute()
# path = str(path) + '/categ_list.txt'
categ_list = ['eat','ent','coffee','transport', 'sport', 'clothers','other']
string_out = ' '.join(categ_list)
f = open('categ_list.txt','w')
f.write(string_out)
f.close()

string_in = input("Input command\n")
if string_in == '/cat':
    f = open('categ_list.txt','r')
    for line in f:
        string = line
    print(string)
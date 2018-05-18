import pickling
import getch
import traceback
import nodes

rnodes = pickling.read()

nodes = []
for node in rnodes:
    if '__call__' in dir(node):
        nodes.append(node)
def printOptions():
    print('--options--')
    for index,node in enumerate(nodes):
        print(str(index).rjust(2,'0') + ' ',end = '')
        try:
            print(node.title)
        except Exception:
            print('has no title')


key1 = ''
key2 = ''
while key1!='q' and key2!='q':
    printOptions()
    print('call:')
    key1 = getch.getKey()
    print(key1)
    key2 = getch.getKey()
    print(key2)
    try:
        nodes[(int("".join([key1,key2])))]()
    except Exception:
        traceback.print_exc()

import pickle
import os
import traceback

dir_path = os.path.dirname(os.path.realpath(__file__))
file = os.path.join(dir_path,"db.txt")


#classes
def read():
    try:
        out = pickle.load(file = open(file,'rb'))
        print('>pickle loaded<')
    except Exception:
        out = []
        traceback.print_exc()
        print('>faced exception<')
    return out

def write(array):
    pickle.dump(array, file = open(file,'wb'), protocol = pickle.HIGHEST_PROTOCOL)
    print('>pickle dumped<')
    
def append(node):
    #try:
        #out = pickle.load(file = open(file,'rb'))
        #print('>pickle loaded<')
    #except Exception:
        #out = []
        #traceback.print_exc()
        #print('>faced exception<')
    pickle.dump([node], file = open(file,'ab'), protocol = pickle.HIGHEST_PROTOCOL)
    print('picke appended')
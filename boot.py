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
    except exception:
        out = []
        traceback.print_exc()
        print('>faced exception<')
    return out

def write(array):
    pickle.dump(array, file = open(file,'wb'), protocol = pickle.highest_protocol)
    print('>pickle dumped<')




def boot():
    rnodes = read()
    for node in rnodes:
        try:
            if node.__class__.__name__ == 'Launch':
                node()
                break
        except Exception:
            pass
boot()

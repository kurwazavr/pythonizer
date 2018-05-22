
import pickle
import os
import traceback



class Pickler:
    def setFile(self):
   
        dir_path = os.path.dirname(os.path.realpath(__file__))
        dir_path = os.sep.join(dir_path.split(os.sep)[:-1])
        self.file = os.path.join(dir_path,"db.txt")
    def __init__(self,title = 'Pickler'):
        self.title = title
        self.setFile()
        print('Pickler created with title ' + title)
    
    def read(self):
        try:
            out = pickle.load(file = open(self.file,'rb'))
            print('>pickle loaded<')
        except Exception:
            out = []
            traceback.print_exc()
            print('>faced exception<')
        return out
    
    def write(self,array):
        pickle.dump(array, file = open(self.file,'wb'), protocol = pickle.HIGHEST_PROTOCOL)
        print('>pickle dumped<')
     
    
    



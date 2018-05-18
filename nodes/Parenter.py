
import pickling
import traceback





class Parenter:
    def __init__(self,title = 'Parenter'):
        print('created> '+title)
        self.title = title
        #self.children = []
        
        
    def __call__(self):
        parent = input('parentID:')
        child = input('childID:')
        rnodes = pickling.read()
        try:
            parent = int(parent)
            child = int(child)
            rnodes[parent].setChild(rnodes[child])
            pickling.write(rnodes)
        except Exception:
            traceback.print_exc()
        
        
    #def addChild(self,node):
        #self.children.append(node)
        #print(node.title + ' >is now a child of< ' + self.title)
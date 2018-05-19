import getch
import pickling

class Jumper:
    def __init__(self,title = 'Jumper'):
        self.title = title
        self.children = []
        print('Jumper created with title ' + title)
    def __call__(self):
        
        print('>Jumper started<\n>Jumper has his own children, just pass an empty string(to implement)<\n>empty string to quit')
        id = input('show children of:')
        while id:
            rnodes = pickling.read()
            current = rnodes[int(id)]
            print('children of:'+id+' '+current.title)
            for index,node in enumerate(rnodes):
                
                if node in current.children:
                    try:
                        print(str(index).rjust(4,' ') + ' ',end = '')
                        print(('children:'+ str(len(node.children))).ljust(10,' ') + ' ',end = '')
                        print(node.title)
                    except Exception:
                        print(str(index).rjust(4,' ') + ' ',end = '')
                        print('has no title')

            id = input('show children of:')
        
        
        
    def setChild(self,node):
        if node not in self.children:
            self.children.append(node)
            print(node.title + ' >is now a child of< ' + self.title)
        else:
            self.children.remove(node)
            print(node.title + ' >is no longer a child of< ' + self.title)    


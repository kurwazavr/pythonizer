import pickling
class PrintThemAll:
    def __init__(self,title = 'PrintThemAll'):
        #print('created> '+title)
        self.title = title
        #self.children = []
    def __call__(self):
        for index,node in enumerate(pickling.read()):
            print(str(index).rjust(4,' ') + ' ',end = '')
            try:
                print(node.title)
            except Exception:
                print('has no title')
        #out = input('tell:')
        #print(out)
    #def addChild(self,node):
    #    self.children.append(node)
    #    print(node.title + ' >is now a child of< ' + self.title)
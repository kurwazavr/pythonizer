import pickling



class Search:
    def __init__(self,title = 'Search'):
        self.title = title
        self.children = []
        print('Search created with title ' + title)
    def __call__(self):
        
        print('>Search called<')
        search = input('search:')
        
        rnodes = pickling.read()
        for index,node in enumerate(rnodes):
            if node.title == search:
                try:
                    print(str(index).rjust(4,' ') + ' ',end = '')
                    print(('children:'+ str(len(node.children))).ljust(10,' ') + ' ',end = '')
                    print(node.title)
                except Exception:
                    print(str(index).rjust(4,' ') + ' ',end = '')
                    print('has no title')



    def setChild(self,node):
        if node not in self.children:
            self.children.append(node)
            print(node.title + ' >is now a child of< ' + self.title)
        else:
            self.children.remove(node)
            print(node.title + ' >is no longer a child of< ' + self.title)   
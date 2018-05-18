import getch
import set_time
import traceback
import nodes.Node
import pickling




class Timeline:
    def __init__(self,title = 'Timeline'):
        print('created> '+title)
        self.title = title
        self.children = []
    
    def Marker(self,interactive = False):
        if interactive:
            title = set_time.setTimeInteractive()
        else:
            title = set_time.setTime()
        marker = nodes.Node.Node(title=title)
        #self.setChild(marker)
        return [marker]
        
    def customMarker(self,parent_name = ''):
        if parent_name == '':
            parent_name = input('parent_name:')
        
        if parent_name == 'created':
            marker = self.Marker()[0]

        else:
            marker = self.Marker(interactive = True)[0]
        parent = nodes.Node.Node(title = parent_name)
        parent.setChild(marker)
        return [parent,marker]
        
    def printMarkers(self,specific = ''):
        groups = []
        rnodes = pickling.read()
        for node in rnodes:
            #find yourself created in DB
            if node.__class__.__name__ == 'Timeline':
                first_self = node
                first_self.children.sort(key = lambda x:x.title)
                #append groups [parent_name,marker]
                for child in first_self.children:
                    for node in rnodes:
                        try:
                            #if node.title == 'created':
                            if child in node.children:
                                groups.append([node,child])
                        except Exception:
                            pass
                #append group elements nodes, it'll be [node,parent_name,marker]
                for obj in groups:
                    #found = False
                    for node in rnodes:
                        
                        try:
                            if obj[0] in node.children:
                                obj.insert(0, node)
                                found = True
                                
                        except Exception:
                            pass
                #print(groups)
                for obj in groups:
                    #try is for the case of obj element not having len of 3
                    try:
                        print(obj[2].title + ':' + obj[1].title.ljust(10,' ') + ':' + obj[0].title)
                    except Exception:
                        pass
                
                break
    
    
    
    
    def __call__(self):
        # no way to pass args as you are not going to invoke function, to be changed later to a special "function" mode
        cmds = [self.printMarkers,self.customMarker]
        [print(str(index) + ' ' + cmd.__name__) for index,cmd in enumerate(cmds)]
        key = getch.getKey()
        
        
        try:
        
            out = cmds[int(key)]()
            if out:
                #print(out)
                rnodes = pickling.read()
                for node in rnodes:
                    if node.__class__.__name__ == 'Timeline':
                        timeline = node
                        print('timeline found')
                        break
                else:
                    print('timeline not found')
                timeline.setChild(out[-1])
                rnodes+=out
                pickling.write(rnodes)
        except Exception:
            traceback.print_exc()
        
        
        
    def setChild(self,node):
        if node not in self.children:
            self.children.append(node)
            print(node.title + ' >is now a child of< ' + self.title)
        else:
            self.children.remove(node)
            print(node.title + ' >is no longer a child of< ' + self.title)
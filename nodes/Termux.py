import pickling
import time
import set_time
import getch
import nodes.Node
from subprocess import call

class Vibrate:
    def __init__(self,title = 'vibrate'):
        self.title = title
        self.children = []
        pass
    def setChild(self,node):
        if node not in self.children:
            self.children.append(node)
            print(node.title + ' >is now a child of< ' + self.title)
        else:
            self.children.remove(node)
            print(node.title + ' >is no longer a child of< ' + self.title)

            
class Watcher:
    def __init__(self,title = 'Watcher'):
        self.title = title
        pass
    def findNodes(self):
        rnodes = pickling.read()

        for node in rnodes:
            if node.__class__.__name__ == 'Vibrate':
                for child in node.children:
                    if child.title[:-3]==set_time.setTime()[:-3]:
                        return True
    def __call__(self):
        print('1 for start\n2 for custom time')
        
        key = getch.getKey()
        
        if key == '1':        
            print('Watcher started')
            while True:
                if self.findNodes():
                    duration = 150
                    for x in range(3):
                        call(['termux-vibrate','-d '+str(duration)])
                else:
                    print('last check:'+set_time.setTime())
                time.sleep(60)

            
        elif key == '2':
            rnodes = pickling.read()
            for node in rnodes:
                if node.__class__.__name__ == 'Timeline':
                    timeline  = node
            node = nodes.Node.Node(title = set_time.setTimeInteractive())
            timeline.setChild(node)
            vibrate = Vibrate()
            vibrate.setChild(node)
            rnodes.append(node)
            rnodes.append(vibrate)
            pickling.write(rnodes)


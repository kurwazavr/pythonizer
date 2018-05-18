import pickling
import nodes.Node
import nodes.Timeline
import set_time




class Listener:
    def __init__(self,title = 'Listener'):
        self.title = title
    def __call__(self):

  

        node_title = input('title:')
        while node_title!='':
            rnodes = pickling.read()
            for node in rnodes:
                if node.__class__.__name__ == 'Timeline':
                    timeline = node
                    print('timeline found')
                    break
            else:
                print('timeline not found')
            
            node = nodes.Node.Node(title=node_title)
            #notice parent_name = 'created', special keyword
            parent_marker = timeline.customMarker(parent_name = 'created')
            node.setChild(parent_marker[0])

            rnodes= rnodes + [node] + parent_marker
            #print(timeline.children)
            pickling.write(rnodes)
            node_title = input('title:')
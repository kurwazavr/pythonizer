import pickling
import traceback




class Sorter:
    def __init__(self,title = 'Sorter'):
        print('created> '+title)
        self.title = title
    def __call__(self):
        rnodes  =  pickling.read()
        tmp  = input('parent:')
        
        try:
            tmp = int(tmp)
            rule_true = []
            rule_false = []
            for node in rnodes:
                if node in rnodes[tmp].children:
                    rule_true.append(node)
                else:
                
                    rule_false.append(node)
            print(str(len(rule_true))+' sorted downwards')
            pickling.write(rule_false+rule_true)
            
        except Exception:
            traceback.print_exc()
        
        
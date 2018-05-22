import readline
readline.parse_and_bind('tab: complete')


class AutoComplete:

    def __init__(self, title = 'AutoComplete'):
       self.children = []
       self.title = title
       print('AutoComplete has been created with title ' + title)
    def complete(self, text, state):
        if state == 0:  # on first trigger, build possible matches
            if text:  # cache matches (entries that start with entered text)
                self.matches = [s for s in self.options 
                                    if s and s.startswith(text)]
            else:  # no text entered, all matches possible
                self.matches = self.options[:]

        # return match indexed by state
        try: 
            return self.matches[state]
        except IndexError:
            return None
    def __call__(self,options = []):
        readline.set_completer(self.complete)
        self.options = sorted(options)
        tinput = input('let me autocomplete:')
        return tinput


def out(text):
    print "gimme: %s" % text

"""
    Returns a boolean to say whether a path is 'hidden'
    
    e.g.
    ~/dirA/.dirB/dirC/ => false 
        '.dirB' is hidden hence all children are hidden

"""
def folder_not_hidden(path):
    return '/.' not in path



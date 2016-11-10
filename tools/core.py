
def out(text):
    print "gimme: %s" % text

def folder_not_hidden(path):
    """
    Returns a boolean to say whether a path is 'hidden'

    e.g.
    ~/dirA/.dirB/dirC/ => false
        '.dirB' is hidden hence all children are hidden

    """
    return '/.' not in path


def print_options(paths):
    """ Print each path in a nice format """
    index = 0
    for repo in paths:
        print "\t#%d - \'%s\'" % (index, repo)
        index += 1

def user_input():
    try:
        return raw_input('$ ')
    except KeyboardInterrupt:
        print ''
        out('Cancelled')
        exit(-1)

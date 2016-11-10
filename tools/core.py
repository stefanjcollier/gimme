
def out(text):
    """ A pretty print using the name of the function """
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
    """ A nice controlled method to accept user input handling the KeyboardInterrupt gracefully """
    try:
        return raw_input('$ ')
    except KeyboardInterrupt:
        print ''
        out('Cancelled')
        exit(-1)


def display_usage():
    print "Usage:"
    print "   $gimme <substring>                      # Return the path to the repo that contains that substring"
    print "   $gimme [-f | --force-first] <substring> # Return the first path to the repo that contains that substring"
    print "   $gimme [-a | --add-path] <path>         # Add a path to search tree"
    print "   $gimme -                                # Return the last repo that was searched for"

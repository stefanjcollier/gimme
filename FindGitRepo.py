#!/bin/python2

#
#
#
#
import sys
from os import listdir
from FindGitRepoHelper import *


# Accept all command line arguements
search=' '.join(sys.argv[1:])
if not search:
    out('Not Implemented Yet')
    exit(-99)


# The folder where all the git repos are stored
git = init_git()

# Validate git variable
if not isdir(git):
    out('The folder \'%s\' is not a valid directory' % git)
    exit(-2)

elif listdir(git) == []:
    out('There are no repos in your git folder (%s) ' % git)
    exit(-2)

# Find the repo based on search
repos = get_repos(git)
matchers = [repo for repo in repos if search in repo ]
if len(matchers) == 0:
    out('No repo matches the description \'%s\'' % search)
    exit(-1)

elif len(matchers) == 1:
    print join(git,matchers[0])
    exit(0)

else:
    out('Your search produced more than one repo:')
    for repo in matchers:
        print "\t%s" % repo
    print 'Please be more specific'
    exit(1)



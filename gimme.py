#!/usr/bin/env python

#---
# Description:
#   A script to find a git repository based on a subset of the name
# 
# Usage:
#   $gimme <substring>                      # Return the path to the repo that contains that substring
#   $gimme [-f | --force-first] <substring> # Return the first path to the repo that contains that substring
#   $gimme -                                # Return the last repo that was searched for
#
# Example:
#   $gimme example
#   >/Users/MyUser/Git/my-example-repo/
#
#---

import sys
from tools.core import *
from tools.gitrepo import *
from tools.hist import *

# Find the repo based on search
def find_matching_repo(search, allow_first = False):
    repos = get_repos()

    matchers = [repo for repo in repos if search in repo ]
    if len(matchers) == 0:
        out('No repo matches the description \'%s\'' % search)
        exit(-1)

    #Only found one matching repo
    elif len(matchers) == 1:
        selected_repo = matchers[0]
        save_selected_git_repo(selected_repo)
        exit(0)

    else:
        if allow_first:
            first_repo = matchers[0]
            save_selected_git_repo(first_repo)
            exit(0)
        else:
            out('Your search produced more than one repo:')
            for repo in matchers:
                print "\t\'%s\'" % repo
            print 'Please be more specific'
            exit(1)

def display_usage():
    print "Usage:"
    print "   $gimme <substring>                      # Return the path to the repo that contains that substring"
    print "   $gimme [-f | --force-first] <substring> # Return the first path to the repo that contains that substring"
    print "   $gimme -                                # Return the last repo that was searched for"

if __name__ == '__main__':
    if len(sys.argv) < 2 or sys.argv[1] == '--help':
        display_usage()
        exit(5)
    
    first_arg = sys.argv[1]

    if first_arg == '-':
        if not get_last_git_repo():
            out('You have not yet used \'gimme\' to get to a repo')
            exit(2)
     
    elif first_arg in ['-f', '--force-first']:
        search=' '.join(sys.argv[2:])
        find_matching_repo(search, True)

    else:
        search=' '.join(sys.argv[1:]) 
        find_matching_repo(search)



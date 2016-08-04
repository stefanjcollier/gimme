#!/bin/python2

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
# Requirements:
#       ?None Yet?
#
#---

import sys
from os import listdir
from tools.core import *
from tools.gitrepo import *
from tools.hist import *

def ensure_git_home():
    # The folder where all the git repos are stored
    git = locate_git()

    # Validate git variable
    if not isdir(git):
        out('The folder \'%s\' is not a valid directory' % git)
        exit(-2)

    elif listdir(git) == []:
        out('There are no repos in your git folder (%s) ' % git)
        exit(-2)

    else:
        return git

# Find the repo based on search
def find_matching_repo(git, search, allow_first = False):
    repos = get_repos(git)
    matchers = [repo for repo in repos if search in repo ]
    if len(matchers) == 0:
        out('No repo matches the description \'%s\'' % search)
        exit(-1)

    elif len(matchers) == 1:
        selected_repo = join(git,matchers[0])
        save_selected_git_repo(selected_repo)
        exit(0)

    else:
        if allow_first:
            first_repo = join(git,matchers[0])
            save_selected_git_repo(selected_repo)
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
        exit(0)
    
    first_arg = sys.argv[1]
    git_home = ensure_git_home()
    assert_file()

    if first_arg == '-':
        if not get_last_git_repo():
            out('You have not yet used \'gimme\' to get to a repo')
     
    elif first_arg in ['-f', '--force-first']:
        search=' '.join(sys.argv[2:])
        find_matching_repo(git_home, search, True)

    else:
        search=' '.join(sys.argv[1:]) 
        find_matching_repo(git_home, search)

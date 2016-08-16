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
import learn

def print_options(paths):   
    index = 0
    for repo in paths:
        print "\t#%d - \'%s\'" % (index, repo)
        index += 1

def substring_of_any_path(substring, paths):
    return substring != '' and any([substring in path for path in paths])

def option_in_range(option,paths):
    return option.isdigit() and int(option) in range(len(paths))

def narrow_search_down(paths):
    print_options(paths)
    print 'Select an option by entering an option, e.g. $ 2'
    print '  or enter another substring to narrow it down e.g. $ chef'
    choice = raw_input('$ ')
    while not (substring_of_any_path(choice, paths) or option_in_range(choice, paths)):
        print 'Enter a valid string (see above).'
        choice = raw_input('$ ')
        
    if option_in_range(choice, paths):
        index = int(choice)
        path = paths[index]
        
        learn.choose(path)
        save_selected_git_repo(path)
        exit(0)

    elif substring_of_any_path(choice, paths):
        less_paths = [path for path in paths if choice in path]
        if len(less_paths) == 1:
            selected_repo = less_paths[0]
            learn.choose(path)
            save_selected_git_repo(selected_repo)
            exit(0)
        else:
            narrow_search_down(less_paths)


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
            first_repo = learn.sort(matchers)[0]
            save_selected_git_repo(first_repo)
            exit(0)
        else:
            out('Your search produced more than one repo:')
            print 'Please be more specific'
            narrow_search_down(matchers)
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



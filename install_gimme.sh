#!/bin/bash

#---
# Description:
#   Installs 'gimme' by including the structure:
#   
#   ~/
#   |-.stools_config/
#       |-gimme/
#           |-git_home_loc.txt
#           |-gimme_hist.txt
#
# Usage:
#    ./install_gimme.sh             #Installs the gimme command and asks for user input
#    ./install_gimme.sh <path>      #Installs the gimme command and asks for user input
#
#  where <path> is the path to the users folder with all their git repos
#---

set -x
mkdir ~/.stools_config && true
mkdir ~/.stools_config/gimme && true
touch ~/.stools_config/gimme/git_home_loc.txt
touch ~/.stools_config/gimme/gimme_hist.txt
set +x


if [ -z $1 ]; then
    while [ 1 ]; do
        echo 'Please choose a path for your git repo'
        git_home=`read`
        
        # Ensure it's real
        if [ -d $git_home ]; then
            break
        fi
    done
else
    git_home=$1
    if [ ! -d $git_home ]; then
        echo 'gimme: That is not a valid directory'
        exit -1
    fi
fi
cat $git_home > ~/.stools_config/gimme/git_home_loc.txt
echo 'gimme: Install complete'


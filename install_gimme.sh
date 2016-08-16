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
#    ./install_gimme.sh       #Installs the gimme command
#
#---
echo '============================='
echo '      Installing gimme'
echo '============================='
echo '+Making folders'
mkdir ~/.stools_config && true
mkdir ~/.stools_config/gimme && true

echo '+Creating files'
touch ~/.stools_config/gimme/gimme_hist.txt
touch ~/.stools_config/gimme/votes.csv

echo 'install_gimme: Install complete'
echo ''
echo '============================='
echo '  Add this to your .bashrc'
echo '============================='
echo ''
echo "function gimme {"
echo "   python ${PWD}/gimme.py \$*"
echo "   if [ \$? -eq 0  ]; then"
echo "       cd \`cat ~/.stools_config/gimme/gimme_hist.txt\`"
echo "   fi"
echo "}"

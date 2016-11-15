# gimme
A simple command line tool to change between git repositories.
Using a python script to find a git repository based on a subset of the name.

## Usage:
```
   $gimme <substring>                      # Return the path to the repo that contains that substring
   $gimme [-f | --force-first] <substring> # Return the first path to the repo that contains that substring
   $gimme [-a | --add-path] <path>         # Add a path to search tree
   $gimme -                                # Return the last repo that was searched for
```
## Examples:
Using gimme when there is only one matching result
``` bash 
   stcollier@StefTop:~$gimme example
   Path set to /Users/stcollier/git/my-example-repo/
   stcollier:~/git/my-example-repo $ 
```
Or when there is more than one initial matching result
```
stcollier@StefTop:~$ gimme agent
gimme: Your search produced more than one repo:
Please be more specific
        #0 - '/home/stcollier/intelligent-agents-adx-agent/'
        #1 - '/home/stcollier/sneakyprojects/bond-agent/'
Select an option by entering an option, e.g. $ 2
  or enter another substring to narrow it down e.g. $ chef
$ bond
Path set to /home/stcollier/sneakyprojects/bond-agent/
stcollier@StefTop:/home/stcollier/sneakyprojects/bond-agent $
```
## Installation:
Run the `install_gimme.sh` from within the gimme folder
``` bash 
git clone https://github.com/stefanjcollier/gimme.git
cd gimme
./install_gimme.sh
```
Then copy the outputted line to your `.bashrc` or likewise file
``` bash
source ~/.stools_config/gimme/gimme_function.sh
```
[Example Installation](https://github.com/stefanjcollier/gimme/blob/master/pages/exmaple_install.md)


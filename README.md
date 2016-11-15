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
## Example:
``` bash 
   stefan:~$gimme example
   Path set to /Users/stefan/Git/my-example-repo/
   stefan:~/Git/my-example-repo/$ 
```
## Installation:
Run the `install_gimme.sh` from within the gimme folder
Then copy the outputted line to your `.bashrc` or likewise file
``` bash 
git clone https://github.com/stefanjcollier/gimme.git
cd gimme
./install_gimme.sh
```
[Example Installation](https://github.com/stefanjcollier/gimme/blob/master/pages/exmaple_install.md)


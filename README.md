# gimme
A simple command line tool to change between git repositories.
Using a python script to find a git repository based on a subset of the name.

## Usage:
```
   $gimme <substring>                      # Return the path to the repo that contains that substring
   $gimme [-f | --force-first] <substring> # Return the first path to the repo that contains that substring
   $gimme -                                # Return the last repo that was searched for
```
## Example:
``` bash 
   stefan:~$gimme example
   Path set to /Users/stefan/Git/my-example-repo/
   stefan:~/Git/my-example-repo/$ 
```
## Installation:
Run the `install_gimme.sh` with the location of the folder that contains a collection of your git repos.
Then copy the outputted function to your `.bashrc`.
``` bash 
git clone https://github.com/stefanjcollier/gimme.git
./install_gimme.sh /Path/to/git/collection/
```
[Example Installation](https://github.com/stefanjcollier/gimme/blob/master/pages/exmaple_install.md)


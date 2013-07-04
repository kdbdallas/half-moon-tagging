# tag

## Danger

Here be dragons. You use this at your own risk.

## Install

    pip install --user git+https://github.com/schwa/half-moon-tagging.git
    
## Usage

    $ tag -h
    tag - manipulate OS X file system flags

    Usage:
      tag <path>
      tag --list <path>...
      tag --add <tag> <path>...
      tag --set <tag> <path>...
      tag --remove <tag> <path>...
      tag (-h | --help)
      tag --version

    Options:
      -l --list          TODO
      -a --add=<tag>     One or more tags to add to paths
      -r --set=<tag>     TODO
      -r --remove=<tag>  TODO
      -h --help          Show this screen.
      --version          Show version.
    $ touch example.txt
    $ tag --list example.txt
    example.txt ()
    $ tag --set Green example.txt
    $ tag --list example.txt
    example.txt (Green)
    $ tag --add Examples example.txt
    $ tag --list example.txt
    example.txt (Green, Examples)
    $ tag --set Red,Green,Purple example.txt
    $ tag --list example.txt
    example.txt (Red, Green, Purple)

## License
    
    BSD 2-clause


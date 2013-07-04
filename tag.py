"""tag - Mavericks command line tool for tagging files

Usage:
  tag <path>
  tag --list <path>...
  tag --add <tag> <path>...
  tag --set <tag> <path>...
  tag --remove <tag> <path>...
  tag (-h | --help)
  tag --version

Options:
  -l --list          List all tags at each path
  -a --add=<tag>     Add one or more (comma separated) tags to paths
  -r --set=<tag>     Set one or more (comma separated) tags on paths
  -r --remove=<tag>  Remove one or more (comma separated) tags from paths
  -h --help          Show this screen.
  --version          Show version.
"""

__author__ = 'schwa'

from docopt import docopt
import sys
# import shlex
# import subprocess

import biplist # pip install --user biplist
import xattr # pip install --user xattr

#def raw_tag_for_tag(tag):
#    output = subprocess.check_output(['mdfind', 'kMDItemUserTags == \'{}\''.format(tag)])
#    sample_path = output.split('\n')[0]
#    if not sample_path:
#        return tag
#    raw_tag = [raw_tag for raw_tag  in raw_tags(sample_path) if raw_tag.startswith(tag)][0]
#    return raw_tag

def get_raw_tags(path):
    if 'com.apple.metadata:_kMDItemUserTags' in xattr.listxattr(path):
        d = xattr.getxattr(path, 'com.apple.metadata:_kMDItemUserTags')
        d = biplist.readPlistFromString(d)
        return d
    else:
        return []

def get_tags(path):
    tags = get_raw_tags(path)
    tags = [tag.split('\n')[0] for tag in tags]
    return tags

def set_tags(path, tags):
    data = biplist.writePlistToString(tags)
    xattr.setxattr(path, 'com.apple.metadata:_kMDItemUserTags', data)

def add_tag(path, tag):
    tags = get_tags(path)
    if tag in tags:
        return
    set_tags(path, tags)

def add_tags(path, tags):
    old_tags = get_tags(path)
    new_tags = old_tags + [tag for tag in tags if tag not in old_tags]
    set_tags(path, new_tags)

def remove_tag(path, tag):
    tags = get_tags(path)
    for tag in tags:
        tags.remove(tag)
    set_tags(path, tags)

def remove_tags(path, tags):
    old_tags = get_tags(path)
    new_tags = [tag for tag in old_tags if tag not in tags]
    set_tags(path, new_tags)

def split_tags(s):
    tags = s.split(',')
    tags = [tag.strip() for tag in tags]
    return tags

def main(argv = None):
    #    argv = shlex.split(raw_input('$ tag '))
    arguments = docopt(__doc__, argv = argv, version='tag 1.0a1')
    if arguments['--list']:
        for path in arguments['<path>']:
            print '{} ({})'.format(path, ', '.join(get_tags(path)))
    elif arguments['--add']:
        tags = split_tags(arguments['--add'])
        for path in arguments['<path>']:
            add_tags(path, tags)
    elif arguments['--set']:
        tags = split_tags(arguments['--set'])
        for path in arguments['<path>']:
            set_tags(path, tags)
    elif arguments['--remove']:
        tags = split_tags(arguments['--remove'])
        for path in arguments['<path>']:
            remove_tags(path, tags)
    elif arguments['--list']:
        for path in arguments['<path>']:
            print '{} ({})'.format(path, ', '.join(get_tags(path)))

if __name__ == '__main__':
    main()

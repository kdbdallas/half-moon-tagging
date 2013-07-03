__author__ = 'schwa'

import biplist # pip install --user biplist
import xattr # pip install --user xattr
import subprocess

def raw_tag_for_tag(tag):
    output = subprocess.check_output(['mdfind', 'kMDItemUserTags == \'{}\''.format(tag)])
    sample_path = output.split('\n')[0]
    if not sample_path:
        return tag
    raw_tag = [raw_tag for raw_tag  in raw_tags(sample_path) if raw_tag.startswith(tag)][0]
    return raw_tag

def raw_tags(path):
    if 'com.apple.metadata:_kMDItemUserTags' in xattr.listxattr(path):
        d = xattr.getxattr(path, 'com.apple.metadata:_kMDItemUserTags')
        d = biplist.readPlistFromString(d)
        return d
    else:
        return []

def add_raw_tag(path, tag):
    d = raw_tags(path)
    if tag in d:
        return
    d.append(tag)
    d = biplist.writePlistToString(d)
    xattr.setxattr(path, 'com.apple.metadata:_kMDItemUserTags', d)

def tags(path):
    return raw_tags(path)

def remove_tag(path, tag):
    pass

def set_tags(path, tags):
    pass

def add_tag(path, tag):
    add_raw_tag(path, tag)

add_raw_tag('.', 'Work')
print tags('.')

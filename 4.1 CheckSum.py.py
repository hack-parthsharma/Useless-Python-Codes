#!/usr/bin/python

import sys,hashlib

if len(sys.argv) != 2:
    print "[!]python CheckSum.py filename"
    sys.exit()
filename = sys.argv[1]
def md5(string):
    return hashlib.md5(string).hexdigest()

def sha1(string):
    return hashlib.sha1(string).hexdigest()
fi = open(filename,"rb")
data = fi.read()
final_md5_hash = md5(data)
final_sha1_hash = sha1(data)
print "MD5 -- > {0} : {1}".format(filename,final_md5_hash)
print "SHA1 -- > {0} : {1}".format(filename,final_sha1_hash)

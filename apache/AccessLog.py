import fileinput
import re
import os
try: import simplejson as json
except ImportError: import json

#read input file and return entries' Dict Object
def readfile(file):
    filecontent = {}
    index = 0
    #check necessary file size checking
    statinfo = os.stat(file)

    #just a guestimate. I believe a single entry contains atleast 150 chars
    if statinfo.st_size < 150:
        print "Not a valid access_log file. It does not have enough data"
    else:
        for line in fileinput.input(file):
            index = index+1
            if line != "\n": #don't read newlines
                filecontent[index] = line2dict(line)

        fileinput.close()
    return filecontent

#gets a line of string from Log and convert it into Dict Object
def line2dict(line):
    #Snippet, thanks to http://www.seehuhn.de/blog/52
    parts = [
    r'(?P<HOST>\S+)',                   # host %h
    r'(?P<IDENTITY>\S+)',               # indent %l (unused)
    r'(?P<USER>\S+)',                   # user %u
    r'\[(?P<TIME>.+)\]',                # time %t
    r'"(?P<REQUEST>.+)"',               # request "%r"
    r'(?P<STATUS>[0-9]+)',              # status %>s
    r'(?P<SIZE>\S+)',                   # size %b (careful, can be '-')
    r'"(?P<REFERER>.*)"',               # referer "%{Referer}i"
    r'"(?P<USERAGENT>.*)"',                 # user agent "%{User-agent}i"
]
    pattern = re.compile(r'\s+'.join(parts)+r'\s*\Z')
    m = pattern.match(line)
    res = m.groupdict()
    return res

#to get jSon of entire Log
#returns JSON object
def toJson(file):
    #get dict object for each entry
    entries = readfile(file)
    return json.JSONEncoder().encode(entries)

    
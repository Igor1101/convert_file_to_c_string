#!/usr/bin/python
import sys
if len(sys.argv)==1:
    sys.stderr.write("select file, exitinig")
    exit(1)
try:
    f=open(sys.argv[1])
except IOError:
    sys.stderr.write("no such file:{}".format(sys.argv[1]))
    exit(1)
fmodif=str()
for string in f.read():
    fmodif += string.replace("\\","\\\\")\
            .replace("\n","\\n")\
            .replace("\"","\\\"")\
            .replace("\'", "\\\'")\
            .replace("!","\!")\
            .replace("?","\?")\
            .replace("\r", "\\\r")\
            .replace("\t", "\\\t")\
            .replace("\v", "\\\v")
print("=\"{}\";".format(fmodif))

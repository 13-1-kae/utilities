import os
import sys
import argparse
def dirr(a):
    b=os.listdir(a)
    c=b.split('/')
    l=len(c)
    for i in range (l):
        d=os.path.join(a, c[i])
        if os.path.isfile(d):
            print(c[i])
        else:
            dirr(d)
    return ''


parser = argparse.ArgumentParser
parser.add_argument('pth', type=str )
args=parser.parse_args()
pth=args.pth
s1=os.path.abspath(pth)
if os.path.isfile(s1):
    print(s1)
else:
    print(s1)
    dirr(s1)

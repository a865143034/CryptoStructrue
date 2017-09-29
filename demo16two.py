import re,pprint
from Crypto.Util import strxor
import base64

with open("ex6.txt","r") as fp:
    wenben=[base64.b64decode(i).encode('hex') for i in fp.readlines()]
    wenben="".join(wenben)
G=[]
for z in set(re.findall(r'(.{2})',wenben)):
    loc=[0]+[s.start() for s in re.finditer(z,wenben)]
    G +=[j-i for i,j in zip(loc,loc[1:])]
pprint.pprint(sorted([(j,i) for (i,j) in [[i,sum([j for j in G if j%i==0 and j])] for i in range(1,41)]],reverse=True))

Score=0
for Keylen in range(1,41):
    Key=['*'] *Keylen
    Csplit=[re.findall(r'(.{2})',z) for z in re.findall(r'(.{'+str(Keylen*2)+'})',wenben)]
    Transpose = map(list,[zip(*Csplit)])[0]
    for i in range(Keylen):
        m =0
        for k in range(255):
            score=len(re.findall(r'[a-zA-Z ,\.;?!:]',"".join([strxor.strxor(c.decode('hex'),chr(k)) for c in Transpose[i]])))
            if m<score:
                m=score
                Key[i]= chr(k).encode('hex')

    key = str("".join(Key).decode('hex'))*10000
    m= strxor.strxor(key[:len(wenben.decode('hex'))],wenben.decode('hex'))
    n=len(re.findall('[a-zA-Z]',m))
    if n>Score:
        Score=n
        M=m
        l=Keylen
    K=str("".join(Key).decode('hex'))
print l
print K
print M
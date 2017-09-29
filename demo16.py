import re
import base64
with open("ex6.txt","r") as fp:
    wenben=[base64.b64decode(i) for i in fp.readlines()]
wenben="".join(wenben)

def hanming(x,y):
    num=0
    for i in range(0,len(x)):
        t=ord(x[i])^ord(y[i])
        while t:
           if t&1 : num+=1
           t>>=1
    return num

print hanming("this is a test","wokka wokka!!!")

for i in range(1,40):
    str1=[]
    str2=[]
    for j in range(0,i): str1+=[wenben[j]]
    for j in range(i,2*i): str2+=[wenben[j]]
    str1="".join(str1)
    str2="".join(str2)
    x=float(hanming(str1,str2))/i
    print i,x

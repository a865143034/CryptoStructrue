#coding=utf-8
import re
#with open("ex4.txt") as fp:
#wenben=[i for i in open("ex4.txt").readlines()]
wenben=[]
for i in open("ex4.txt","r").readlines():
    wenben+=[i.replace("\n","")] #序列相加
#str1="1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
score=0
#nn=0
for k in wenben:
    for i in range(0,129):
        tmp=[]
        for j in re.findall(".{2}",k):#任意两个字符的字符串
            tmp += chr(i^int(j,16))
        tmpstr = "".join(tmp)
        num=0
        for j in range(0,len(tmpstr)):
            if tmpstr[j]>='a'and tmpstr[j]<='z':#or tmpstr[j]>='A'and tmpstr[j]<='Z':
                num+=1
        if num>score:
            #print tmpstr
            #if num ==score and num >5:
            #    print tmpstr
            #nn+=1
            score=num#用于更新用
            ansstr=tmpstr
            c=k
            key=chr(i)
#print nn
print c
print key
print ansstr
#print re.findall(".{2}",M)
#print len(re.findall(".{2}",M))
#print type(re.findall("[a-zA-z]",tmpstr))
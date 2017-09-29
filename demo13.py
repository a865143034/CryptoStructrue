#coding=utf-8
import re
str="1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
score=0
for i in range(0,129):
    tmp=[]
    for j in re.findall(".{2}",str):#任意两个字符的字符串
        tmp += chr(i^int(j,16))
    tmpstr = "".join(tmp)
    num=0
    for j in range(0,len(tmpstr)):
        if tmpstr[j]>='a'and tmpstr[j]<='z':#or tmpstr[j]>='A'and tmpstr[j]<='Z':
            num+=1
    if num>score:
        #print tmpstr
        score=num#用于更新用
        ansstr=tmpstr
        key=chr(i)
print key
print ansstr

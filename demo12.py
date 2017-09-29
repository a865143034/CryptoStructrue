#coding=utf-8
import base64
import re
#异或操作无论对什么数都是以二进制的形式实现，所以无所谓进制
#str1=long("1c0111001f010100061a024b53535009181c",16)
#str2=long("686974207468652062756c6c277320657965",16)
str1="1c0111001f010100061a024b53535009181c".decode('hex')
str2="686974207468652062756c6c277320657965".decode('hex')
str3=[]
for i in range(0,len(str1)):
    str3+=[chr(ord(str1[i])^ord(str2[i]))]
str3="".join(str3)
print str3.encode('hex')

#str=str1^str2
#print hex(str)
#print str



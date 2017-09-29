import re
str1="Burning 'em, if you ain't quick and nimble I go crazy when I hear a cymbal"
str2="ICE"*200
str3=[]
for i in range(0,len(str1)):
    str3 +=[(chr(ord(str1[i])^ord(str2[i])))]
print "".join(str3).encode('hex')
#for i in range(0,len(str1)):
#    str3 +=[(hex(ord(str1[i])^ord(str2[i])))]
#print "".join(str3)
import re
with open("ex8.txt","r") as fp:
    wenben=[i.replace("\n","")  for i in fp.readlines()]
for ecb in wenben:
    block =re.findall(".{16}",ecb)
    if len(block)-len(set(block)):
        print ecb

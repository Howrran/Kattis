import re

str = input()

result = re.findall(r'ss',str)
if not result:
    print('no hiss')
else:
    print("hiss")
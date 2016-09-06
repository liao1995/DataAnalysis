import re
myString = 'From: 16s103157@stu.hit.edu.cn'
result = re.search('([\w.-]+)@([\w.-]+)', myString)
if result:
	print (result.group(0))
	print (result.group(1))
	print (result.group(2))

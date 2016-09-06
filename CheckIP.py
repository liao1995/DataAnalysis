import re
isIP = re.compile('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
myString = " Your IP is: 192.168.1.254 "
result = re.findall(isIP, myString)
print(result)

import re
myString = "01/04/2001"
isDate = re.match('[0-1][0-9]\/[0-3][0-9]\/[1-2][0-9]{3}', myString)
if isDate:
	print("valid")
else:
	print("invalid")

from xml.etree import ElementTree
with open("pokemon.xml") as f:
	doc = ElementTree.parse(f)
	for node in doc.findall('row'):
		print("")
		print("id: {0}".format(node.find('id').text))
		print("typeTwo: {0}".format(node.find('typeTwo').text))
		print("name: {0}".format(node.find('name').text))
		print("type: {0}".format(node.find('type').text))

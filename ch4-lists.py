hosts = ['Dolores', 'Clementine', 'Teddy', 'Peter', 'Maeve', 'Angela', 'Lawrence']

def printHostNamesV1(listOfNames):
	for i in range(len(listOfNames)):
		print(listOfNames[i])

def printHostNamesV2(listOfNames):
	for host in listOfNames:
		print(host)


printHostNamesV1(hosts)
print("-----------------")
printHostNamesV2(hosts)		
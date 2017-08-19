btree = {
	5 : (3, 7),
	3 : (2, 4),
	7 : (6, 8)
}

ntree = {
	'a' : ['b', 'c', 'd'],
	'b' : ['e', 'f', 'g'],
	'c' : ['h', 'i'],
	'd' : ['j', 'k', 'l']
}

def inorder(x):
	if x not in ntree:
		print(x)
	else:
		print(x)
		for i in ntree[x]:
			inorder(i)
			
			
inorder('a')

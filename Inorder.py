#INORDER TRAVERSAL OF N-ARY TREE IN PYTHON

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

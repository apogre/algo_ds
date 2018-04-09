class Node:
	def __init__(self):
		self.left = None
		self.right = None

def find_height(root):
	if root == None: return 0
	return max(find_height(root.left),find_height(root.right))+1



a = Node()
b = Node()
c = Node()
d = Node()
e = Node()

a.left = b
b.left = c
c.right = d
b.right = e

print("Tree height:", find_height(a))
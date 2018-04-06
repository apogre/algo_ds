class Node(object):
	def __init__(self, char: str):
		self.child = []
		self.counter = 1
		self.end_of_word = False
		self.char = char

def add_word(root, word):
	node = root
	found_in_child = False
	for char in word:
		for child in node.child:
			if child.char == char:
				child.counter += 1
				node = child
				found_in_child = True
				break
		if not found_in_child:
			new_node = Node(char)
			node.child.append(char)
			node = new_node
	node.end_of_word = True

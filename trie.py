class Node(object):
	def __init__(self, letter):
		self.children = []
		self.counter = 1
		self.end_of_word = False
		self.letter = letter

def add_word(root, word):
	node = root
	for letter in word:
		found_in_children = False
		for child in node.children:
			print child.letter,letter, "checking nodes"
			if child.letter == letter:
				print "increasing counter"
				child.counter += 1
				node = child
				found_in_children = True
				break
		if not found_in_children:
			print "creating node", letter
			new_node = Node(letter)
			node.children.append(new_node)
			node = new_node
	node.end_of_word = True

def find_prefixes(root, word):
	prefixes = []
	print root.letter
	node = root
	if not root.children: return False

	for letter in word:
		print letter
		for child in node.children:
			print child.letter, child.counter
			if child.letter == letter:
				prefixes.append(child.letter)
				if child.counter == 1 or child.end_of_word:
					return ''.join(prefixes)
				else:
					node = child
					break
			else:
				pass
	if prefixes:
		return ''.join(prefixes)
	return -1


root = Node('*')
add_word(root,'zebra')
add_word(root,'dog')
add_word(root,'doug')

print find_prefixes(root, 'zebra')
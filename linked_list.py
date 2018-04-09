class Node:
	def __init__(self,val):
		self.val = val
		self.next = None


class Linked_list:
	def __init__(self):
		self.head = None

	def add_node(self,obj):
		new_node = Node(obj)
		new_node.next = self.head
		self.head = new_node

	def print_list(self):
		temp = self.head
		while temp:
			print temp.val
			temp = temp.next

	def reverse_list(self):
		prev = None
		curr = self.head
		while curr:
			next = curr.next
			curr.next = prev
			prev = curr
			curr = next
		self.head = prev

	def _reverse(self, prev=None):
		node = self.head
		print node.val
		if not node: return prev
		next = node.next
		node.next = prev
		self.head = next
		return self._reverse(node)


l = Linked_list()
l.add_node(1)
l.add_node(2)
l.add_node(3)
l.add_node(4)

l.print_list()
print "==="
l.reverse_list()
l.print_list()
print "==="
l._reverse()
l.print_list()
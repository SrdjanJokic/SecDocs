import os

class Node:
	def __init__(self, name, link = None):
		self.name = name
		self.link = link
		self.children = []

	def print(self, indentation_lvl):
		for lvl in range(0, indentation_lvl):
			print('\t', end='')

		if (self.link != None):
			print(f"- ({self.name})[{self.link}]")
		else:
			print(f"- {self.name}")

local_path_to_docs = '../Documents/'

def print_tree(root):
	stack = []
	stack.append(root)

	while (len(stack) != 0):
		next = stack.pop()
		while (next != None):
			next.print(0)
			for i in range (len(next.children) - 1, 0, -1):
				stack.append(next.children[i])
			if (len(next.children) == 0):
				next = None
			else:
				next = next.children[0]

def create_tree():
	root = Node("Root")
	stack = []
	stack.append(root)
	for path, subdirs, files in os.walk(local_path_to_docs): #pre-order traversal
		node = stack.pop()

		for i in range (len(subdirs) - 1, -1, -1):
			subdir_node = Node(subdirs[i])
			node.children.append(subdir_node)
			stack.append(subdir_node)

		for file in files:
			file_path = os.path.join(path, file)
			file_name = extract_file_name(file_path)
			file_node = Node(file_name, file_path)
			node.children.append(file_node)

	return root

# Extracts file name (without extension) from given path
def extract_file_name(path):
	base_path = os.path.basename(path)
	file_name = os.path.splitext(base_path)[0]
	return file_name

if __name__ == "__main__":
	root = create_tree()
	print_tree(root)

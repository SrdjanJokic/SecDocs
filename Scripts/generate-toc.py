import os
import re

class Node:
	def __init__(self, name, link = None):
		self.name = name
		self.link = link
		self.children = []

	# Adjusted for .md documents
	def __str__(self):
		if (self.link != None):
			return f"- [{self.name}]({self.link})"
		else:
			return f"- {self.name}"

class Tree:
	def __init__(self, init_path):
		self.root = Node("Root")
		stack = []
		stack.append(self.root)

		# Traverses the file system in pre-order format
		for path, subdirs, files in os.walk(init_path):
			print(path)
			node = stack.pop()

			# Add all subdirectories as knots
			for i in range (len(subdirs) - 1, -1, -1):
				subdir_node = Node(subdirs[i])
				node.children.append(subdir_node)
				stack.append(subdir_node)

			# Add all files as leaves
			for file in files:
				file_path = os.path.join(path, file)
				file_name = os.path.splitext(os.path.basename(file_path))[0]
				file_node = Node(file_name, file_path)
				node.children.append(file_node)

	# Pre-order traversal print
	def __str__(self):
		output = ""
		nodes_stack = []
		levels_stack = []

		nodes_stack.append(self.root)
		levels_stack.append(-1)

		while (len(nodes_stack) != 0):
			next_node = nodes_stack.pop()
			indent_lvl = levels_stack.pop()

			while (next_node != None):
				for i in range(0, indent_lvl):
					output += '\t'

				if(next_node != self.root):
					output += f"{next_node}\n"

				for i in range (len(next_node.children) - 1, 0, -1):
					nodes_stack.append(next_node.children[i])
					levels_stack.append(indent_lvl + 1)

				if (len(next_node.children) == 0):
					next_node = None
				else:
					next_node = next_node.children[0]
					indent_lvl += 1

		return output

local_path_to_docs = "../Documents/"
local_path_to_readme = "../README.md"
regex_prefix = "<!--START-TOC-->"
regex_suffix = "<!--END-TOC-->"

def update_tos(tos):
	with open(local_path_to_readme, 'r') as readme:
		data = readme.read()

	# Everything between TOC tags (including new lines)
	pattern = regex_prefix + "((.|\n|\r)*)" + regex_suffix
	new_tos = f"{regex_prefix}\n{tos}{regex_suffix}"
	new_data = re.sub(pattern, new_tos, data)

	with open(local_path_to_readme, 'w') as readme:
		readme.write(new_data)

if __name__ == "__main__":
	file_tree = Tree(local_path_to_docs)
	update_tos(str(file_tree))

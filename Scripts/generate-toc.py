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

# Iterates through the path_to_docs dir and collects all subdir and file names
def create_tree():
	root_node = Node("None")
	for path, subdirs, files in os.walk(local_path_to_docs): #pre-order traversal
		print(f"{path}\n\t{subdirs}\n\t\t{files}")
		for file in files:
			file_path = os.path.join(path, file)
			file_name = extract_file_name(file_path)
			file_node = Node(file_name, file_path)

# Extracts file name (without extension) from given path
def extract_file_name(path):
	base_path = os.path.basename(path)
	file_name = os.path.splitext(base_path)[0]
	return file_name

if __name__ == "__main__":
	create_tree()

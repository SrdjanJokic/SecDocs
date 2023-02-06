import os

local_path_to_docs = '../Documents/'

# Iterates through the path_to_docs dir and collects all subdir and file names
def extract_raw_file_structure():
	paths = []
	current_dir = os.path.dirname(os.path.abspath(__file__))
	# path_to_docs = f"{current_dir}/{local_path_to_docs}"
	path_to_docs = local_path_to_docs
	for path, subdirs, files in os.walk(path_to_docs):
		for file in files:
			file_path = os.path.join(path, file)
			paths.append(file_path)

	return paths

# Extracts file name (without extension) from given path
def extract_file_name(path):
	base_path = os.path.basename(path)
	file_name = os.path.splitext(base_path)[0]
	return file_name

# Creates a dict of clean file names and their paths
def assign_paths_to_file_names(paths):
	paths_with_files = {}
	for path in paths:
		file_name = extract_file_name(path)
		paths_with_files[file_name] = path
	
	return paths_with_files	

if __name__ == "__main__":
	paths = extract_raw_file_structure()
	paths_with_files = assign_paths_to_file_names(paths)
	print(paths_with_files)
	

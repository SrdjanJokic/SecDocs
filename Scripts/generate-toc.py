import os

path_to_docs = '../Documents/'

# Iterates through the path_to_docs dir and collects all subdir and file names
def extract_raw_file_structure():
	paths = []
	for path, subdirs, files in os.walk(path_to_docs):
		for file in files:
			full_file_path = os.path.join(path, file)
			file_path = full_file_path.replace(path_to_docs, "")
			paths.append(file_path)

	print (paths)	

if __name__ == "__main__":
	extract_raw_file_structure()

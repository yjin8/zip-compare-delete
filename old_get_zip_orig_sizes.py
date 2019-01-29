import os
import zipfile

def get_zipped_files(file_path):
	"""
	Constructs a dictionary with (fileName:fileSize) key:value pairs

	:param file_path: path to zipped folder in string format, including the .zip at end
	"""
	zf = zipfile.ZipFile(file_path)
	#zf: an object created from the zipped files

	zipped_files = {}

	for info in zf.infolist():#info: the attributes of all the files in the zf objects
		zipped_files[info.filename] = info.file_size
		#print('\File Name\t', info.filename)
		#print( '\tUncompressed\t', info.file_size, 'bytes')
	return zipped_files

print("ZIPPED FILES---------------------------")
print(get_zipped_files(filePath2))

def get_orig_files(file_path):
	"""
	Constructs a dictionary with (fileName:fileSize) key:value pairs

	:param file_path: path to original folder in string format
	"""
	orig_files = {}
	for root, directories, files in os.walk(file_path):
		for filename in files:
            # join the two strings in order to form the full filepath.
			filepath = os.path.join(root, filename)
			orig_files[filename] = os.path.getsize(filepath)
            #file_paths.append(filepath)
	return orig_files

print("ORIG FILES--------------------------------")
print(get_orig_files(filePath0))
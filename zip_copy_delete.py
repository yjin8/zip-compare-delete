import shutil
import os
import zipfile
from zipfile import ZipFile

#7/23/18 - need to make it easier to modify the script for different months?
#7/23/18 - need write the functions to compare zip + orig files and then delete orig files
#7/24/18 - wrote a simplified function for zipping files
#7/24/18 - still need to write function to delete files --> using functional programmning
#		   to filter the files in a specific time frame and then applying a zip function to it
#		   in other words, applyin map to a filter function (using lambda)
#7/25/18 - figure out path string formating (.zip or not at end)

filePath0 = 'H:/Documents/guestwifi'
filePath1 = 'H:/Documents/coding practice'
filePath2 = 'H:/Documents/testing/guestwifi.zip'
filePath3 = 'H:/Documents/testing/coding practice.zip'

#-------------------------------------------------------#
#

def zip_files(orig_path,zip_path):
	"""
	:param orig_path: the location of the file that needs to be zipped
	:param zip_path: the path of the root directory of your zipped files
	"""
	shutil.make_archive(zip_path[:-4],'zip',orig_path) 
	#zip_path: e.g. 'U:\\PIX-SF\\2018-05\\2018-05-01' (don't include '.zip' at end of first arg)

#zip_files(filePath0,filePath2)

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

'''
	for file in os.listdir(file_path):
		#print(os.path.getsize(filePath1 + '\\' + file))
		orig_files[file] = os.path.getsize(file_path + '\\' + file)


map(lambda x: os.remove(x), get_common_files(d0,d1))

'''

def compare_delete(orig_path, zipped_path):
	dict_orig = get_orig_files(orig_path)
	dict_zipped = get_zipped_files(zipped_path)
	to_delete = []
	for key in dict_orig:
		if key not in dict_zipped:
			continue
		elif dict_orig[key]==dict_zipped[key]:
			to_delete.append(key)
	for root, directories,files in os.walk(orig_path):
		for filename in to_delete:
			filepath = os.path.join(root, filename)
			print(filepath)
			#os.remove(filepath)
	#os.rmdir(orig_path)
	return to_delete

print(compare_delete(filePath0,filePath2))
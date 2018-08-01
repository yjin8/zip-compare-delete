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

filePath1 = 'Z:\\syslog\\PIX-SF\\2018-05-01'
filePath2 = 'U:\\PIX-SF\\2018-05\\2018-05-01.zip'

#-------------------------------------------------------#
#

def zip_files(orig_path,zip_path):
	"""
	:param orig_path: the location of the file that needs to be zipped
	:param zip_path: the path of the root directory of your zipped files
	"""

	shutil.make_archive(zip_path,'zip',orig_path) 
	#zip_path: e.g. 'U:\\PIX-SF\\2018-05\\2018-05-01' (don't include '.zip' at end of first arg)


def get_zipped_files(file_path):
	"""
	Constructs a dictionary with (fileName:fileSize) key:value pairs

	:param file_path: path to zipped folder in string format
	"""
	zf = zipfile.ZipFile(file_path)
	#zf: an object created from the zipped files
	#print(zf.infolist([)1:])

	zipped_files = {}

	for info in zf.infolist()[1:]:#info: the attributes of all the files in the zf objects
		zipped_files[info.filename] = info.file_size
		#print('\File Name\t', info.filename)
		#print( '\tUncompressed\t', info.file_size, 'bytes')
	return zipped_files


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

'''
	for file in os.listdir(file_path):
		#print(os.path.getsize(filePath1 + '\\' + file))
		orig_files[file] = os.path.getsize(file_path + '\\' + file)

'''

def get_common_files(dict0, dict1):
	common_files = dict0.items() & dict1.items()
	return common_files

#print("ORIGINAL FILES")
#print(get_orig_files(filePath1))
print("ZIPPED FILES")
print(get_zipped_files(filePath2))

#a = get_orig_files(filePath1)
b = get_zipped_files(filePath2)
#print(len(a))
print(len(b))

#print(get_common_files(a,b))


#-------------------------------------------------------------------#
# filecmp method of comparing directories, not sure if it's capable #
# of comparing files from a zipped folder and a regular folder      #
#-------------------------------------------------------------------#

'''
d2_contents = [info.filename for info in zf.infolist()[1:]]
print("list contents:")
print(d2_contents)

d1_contents = os.listdir(filePath1)
print("list contents:")
print(d1_contents)

match, mismatch, errors = filecmp.cmpfiles(filePath1, filePath2, d2_contents,shallow = True)
print("matches:")
print(match)
print("mismatches:")
print(mismatch)
print("errors:")
print(errors)
'''
def compare_delete(path1,path2):
	
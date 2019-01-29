import os
from os.path import basename
from zipfile import ZipFile
import zipfile
from zipfile import ZipInfo
import shutil

filePath0 = 'H:/Documents/work/guestwifi'
filePath2 = 'H:/Documents/testing/guestwifi.zip'
'''
def get_all_file_paths(file_path):
 
    # initializing empty file paths list
    file_paths = []
 
    # crawling through directory and subdirectories
    for root, directories, files in os.walk(file_path):
        for filename in files:
            # join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            print(filepath)
            file_paths.append(filepath)

    return file_paths 
'''

#zip_files needs testing
def zip_files(orig_path, zip_path):
	"""
	Zips files into a new directory
	:param orig_path: path to folder to be zipped in string format
	:param zip_path: path to new zipped folder in string format

	"""
	    # initializing empty file paths list
	file_paths_list = []
 
    # crawling through directory and subdirectories
	for root, directories, files in os.walk(orig_path):
		for filename in files:
			# join the two strings in order to form the full filepath.
			filepath = os.path.join(root, filename)
			file_paths_list.append(filepath)
			
    #return file_paths 
	with ZipFile(zip_path, 'w') as zip:
		for file in file_paths_list:
			zip.write(file, arcname=basename(file), compress_type = zipfile.ZIP_DEFLATED)

#zip_files(filePath1,filePath2)


def zip_files_1(orig_path,zip_path):
	shutil.make_archive(zip_path,'zip',orig_path) #

#zip_files_1(filePath1,filePath2)


#shutil.make_archive('H:/coding practice/work','zip','H:/Documents/work')
'''
def get_zipped_files(file_path):
	"""
	Constructs a dictionary with (fileName:fileSize) key:value pairs

	:param file_path: path to zipped folder in string format
	"""
	zf = zipfile.ZipFile(file_path)
	#zf: an object created from the zipped files
	#print(zf.infolist([)1:])

	zipped_files = {}
	#print(zf.getinfo())
	
	for info in zf.infolist():#info: the attributes of all the files in the zf objects
		print(info)
		zipped_files[info.filename] = info.file_size
		print('\tFile Name\t', info.filename)
		print( '\tUncompressed\t', info.file_size, 'bytes')
	return zipped_files


print(get_zipped_files(filePath2))
'''
zipped_sizes = {}

zf = ZipInfo.from_file(filePath2, arcname=None)
print("ZIPPED FILE SIZE")
zipped_sizes[filePath2] = zf.file_size
print(zipped_sizes)

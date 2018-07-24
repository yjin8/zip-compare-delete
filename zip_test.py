import os
from os.path import basename
from zipfile import ZipFile
import zipfile
import shutil

filePath1 = 'H:\\Documents\\work'
filePath2 = 'H:\\work'
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
	shutil.make_archive(zip_path,'zip',orig_path)

zip_files_1(filePath1,filePath2)


#shutil.make_archive('H:/coding practice/work','zip','H:/Documents/work')
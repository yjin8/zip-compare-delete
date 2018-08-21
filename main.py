import os
import shutil
import time
import zipfile

#7/24/18 - still need to write function to delete files --> using functional programmning
#		   to filter the files in a specific time frame and then applying a zip function to it
#		   in other words, applyin map to a filter function (using lambda)
#7/25/18 - figure out path string formating (.zip or not at end)
#-------------------------------------------------------#

DIR_TO_ZIP = "Z:/syslog/149.68.81.76"
YEAR_MONTH = "2017-10"

def zip_files(orig_path,zip_path):
	"""
	:param orig_path: the location of the file that needs to be zipped
	:param zip_path: the path of the root directory of your zipped files
	"""
	shutil.make_archive(zip_path,'zip',orig_path) 
	#zip_path: e.g. 'U:\\PIX-SF\\2018-05\\2018-05-01' (don't include '.zip' at end of first arg)

#zip_files(filePath0,filePath2)


def get_files_to_zip(directory):
	to_zip = []
	for root, directories, files in os.walk(directory):
		for directory in directories:
			path = os.path.join(root,directory)
			if YEAR_MONTH in path:
				#print(path)
				to_zip.append(path)
				#print(to_zip)
		return to_zip

def get_zip_paths(path_list):
	zip_paths = []
	for path in path_list:
		zip_paths.append(path.replace("Z:/syslog/149.68.81.76","U:/149.68.81.76/{}".format(YEAR_MONTH)))
	return zip_paths

def get_zipped_size(directory):
	"""
	returns size of a zipped folder in mB

	:param directory: path to zipped folder in string format, WITHOUT ".zip" at end

	example argument: "U:/149.68.81.76/2017-09/2017-09-01"
	"""
	zf = zipfile.ZipFile(directory+".zip")
	#zf: an object created from the zipped files
	size = float(sum([zinfo.file_size for zinfo in zf.filelist])) / 1000000
	return size


def get_orig_size(directory):
	#returns size of a folder in mB
	#example argument: "Z:/syslog/149.68.81.76\\2017-09-01"
	
	size = float(sum(os.path.getsize(os.path.join(directory,file)) for file in os.listdir(directory))) / 1000000
	return size


def main():
	files_to_zip = get_files_to_zip(DIR_TO_ZIP)#DIR_TO_ZIP needed!!
	zip_paths = get_zip_paths(files_to_zip)

	print(files_to_zip)
	print(zip_paths)

	log = open("zip_log.txt","w")

	if len(files_to_zip) == len(zip_paths):
		for i in range(len(files_to_zip)):
			orig = files_to_zip[i]
			zipped = zip_paths[i]
			zip_files(orig,zipped)
			print("zipped {} to {}".format(orig, zipped))
			log.write("zipped {} to {}\n".format(orig,zipped))

			'''
			if get_orig_size(orig) == get_zipped_size(zipped):
				print("{} and {} are the same size!".format(orig,zipped))
				os.remove(orig)
				print("{} deleted".format(orig))
				log.write("{} deleted\n".format(orig))
			'''
		log.close()
		print("archiving complete")

main()
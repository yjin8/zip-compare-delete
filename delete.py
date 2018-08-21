import os
import shutil
import zipfile
#from zipfile import ZipFile, ZipInfo

def get_files_to_zip(directory):
	to_zip = []
	for root, directories, files in os.walk(directory):
		for directory in directories:
			path = os.path.join(root,directory)
			if "2017-09" in path:
				#print(path)
				to_zip.append(path)
				#print(to_zip)
		return to_zip

def get_zip_paths(path_list):
	zip_paths = []
	for path in path_list:
		zip_paths.append(path.replace("Z:/syslog/149.68.81.76","U:/149.68.81.76/2017-09"))
	return zip_paths

dir_to_zip = "Z:/syslog/149.68.81.76"


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

	files_to_zip = get_files_to_zip(dir_to_zip)
	zip_paths = get_zip_paths(files_to_zip)

	#print(files_to_zip)
	#print(zip_paths)

	log = open("zip_log.txt","w")

	if len(files_to_zip) == len(zip_paths):
		for i in range(len(files_to_zip)):
			orig = files_to_zip[i]
			zipped = zip_paths[i]

			if get_orig_size(orig) == get_zipped_size(zipped):
				print("{} and {} are the same size!".format(orig,zipped))
				os.remove(orig)
				print("{} deleted".format(orig))
				log.write("{} deleted\n".format(orig))
				
	print("deletion complete")
	log.close()

main()
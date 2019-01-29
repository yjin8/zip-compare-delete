import os
import shutil
import zipfile


def zip_files(orig_path,zip_path):
	"""
	:param orig_path: the location of the file that needs to be zipped
	:param zip_path: the path of the root directory of your zipped files
	"""
	shutil.make_archive(zip_path,'zip',orig_path) 
	#zip_path: e.g. 'U:\\PIX-SF\\2018-05\\2018-05-01' (don't include '.zip' at end of first arg)


def get_files_to_zip(directory):
	to_zip = []
	for root, directories, files in os.walk(directory):
		for directory in directories:
			path = os.path.join(root,directory)
			if YEAR_MONTH in path:
				to_zip.append(path)
		return to_zip

def get_zip_paths(path_list):
	zip_paths = []
	for path in path_list:
		zip_paths.append(path.replace("Z:/syslog/149.68.81.76","U:/149.68.81.76/{}".format(YEAR_MONTH)))
	return zip_paths

DIR_TO_ZIP = "Z:/syslog/149.68.81.76"

'''
files_to_zip = get_files_to_zip(dir_to_zip)
print(files_to_zip)

#['Z:/syslog/149.68.80.68\\2017-09-01', 'Z:/syslog/149.68.80.68\\2017-09-02',...]

zip_paths = get_zip_paths(files_to_zip)
print(zip_paths)
#['U:/149.68.81.76/2017-09\\2017-09-01', 'U:/149.68.81.76/2017-09\\2017-09-02',...]

'''

def main():

	files_to_zip = get_files_to_zip(DIR_TO_ZIP)
	zip_paths = get_zip_paths(files_to_zip)

	log = open("zip_log.txt","a")

	if len(files_to_zip) == len(zip_paths):
		for i in range(len(files_to_zip)):
			print("zipping {} to {}".format(files_to_zip[i], zip_paths[i]))
			zip_files(files_to_zip[i],zip_paths[i])
			log.write("zipped {} to {} \n".format(files_to_zip[i], zip_paths[i]))
	print("zipping complete")
	log.close()

main()

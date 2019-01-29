#usr/bin/env python3
import os, shutil, time, zipfile
from datetime import datetime	 

def get_year_month():
	'''
	returns year and month of previous month as a string "YYYY-MM"
	'''
	current_time = time.time()
	month_earlier = current_time - 2592000 
	t = datetime.fromtimestamp(month_earlier)
	YEAR_MONTH = "{}-{:02d}".format(t.year, t.month)
	return YEAR_MONTH

#--------------------------------------------------------------------#
#																	 #
#					ENTER DESIRED INFORMATION BELOW					 #
#																	 #
#--------------------------------------------------------------------#

DIR_TO_ZIP = "Z:\\syslog\\149.68.80.68"
YEAR_MONTH =  "2018-08"	#either use get_year_month() or "YYYY-MM"
DESTINATION_DIR = "U:\\149.68.80.68\\{}".format(YEAR_MONTH)


#--------------------------------------------------------------------#


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

# def get_files_to_zip(directory):
'''
format for @directory:
DIR = "Z:\\syslog\\10.98.254.68\\{}*".format(YEAR_MONTH)

'''
# 	to_zip = glob.glob(directory)
# 	return to_zip

def get_zip_paths(path_list):
	zip_paths = []
	for path in path_list:
		zip_paths.append(path.replace(DIR_TO_ZIP,DESTINATION_DIR))
	return zip_paths


def get_zipped_size(directory):
	"""
	returns size of a zipped folder in mb

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

	#print(files_to_zip)
	#print(zip_paths)

	log = open("zip_log.txt","a")

	if len(files_to_zip) == len(zip_paths):
		for i in range(len(files_to_zip)):
			orig = files_to_zip[i]
			zipped = zip_paths[i]

			#zipping the files
			print("zipping {} to {}.....".format(orig,zipped))
			zip_files(orig,zipped)
			print("zipped")
			log.write("zipped {} to {}\n".format(orig,zipped))

			'''
			#deleting the files - requires admin permission? -probably not
			if get_orig_size(orig) == get_zipped_size(zipped):
				print("{} and {} are both {}mb".format(orig,zipped,get_zipped_size(zipped)))
				shutil.rmtree(orig)
				print("{} deleted".format(orig))
				log.write("{} deleted\n".format(orig))
			'''
		log.close()
		print("archiving complete")

main()

import zipfile
def get_zipped_size(directory):
	"""
	returns size of a zipped folder in mb

	:param directory: path to zipped folder in string format, WITHOUT ".zip" at end

	example argument: "U:/149.68.81.76/2017-09/2017-09-01"
	"""
	zf = zipfile.ZipFile(directory+".zip")
	#zf: an object created from the zipped files
	size = float(sum([zinfo.file_size for zinfo in zf.filelist]))# / 1000000
	return size

print(get_zipped_size("U:\\149.68.80.68\\2017-06\\2017-06-10"))
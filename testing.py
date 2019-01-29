import os,time

filePath0 = 'H:/Documents/work/guestwifi'
#filePath2 = 'H:/Documents/testing/guestwifi.zip'

z_drive_path = 'Z:/syslog/149.68.81.76'

to_zip = []
for root, directories, files in os.walk(z_drive_path):
	for directory in directories:
		path = os.path.join(root,directory)
		#print(path) #Z:/syslog/149.68.8.248\2018-06-01
		if (time.time() - os.path.getctime(path)) >= 2592000:
			to_zip.append(path)


print("DIRECTORIES OLDER THAN 30 DAYS")
print(to_zip)
#---> this takes a long time, more efficient way of finding these directories?


'''
print(os.path.getctime(filePath0)) #1533579300.0
print(time.ctime(os.path.getctime(filePath0)))#Mon Aug  6 14:15:00 2018
print(time.time())#1533581067.9543352
'''

#2592000 = 30 days
#2678400 = 31 days
'''
to_zip_sizes = {}
for p in to_zip:
	to_zip_sizes[os.path.basename(p)] = os.path.getsize(p)

print(to_zip_sizes)

'''

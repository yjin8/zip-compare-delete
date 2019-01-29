import os
#use map() to delete all orig files!!

orig_files = [1,2,3,4,5]
zipped_files = [1,3,5,9]
#squared = list(map(lambda x: x % 2 == 0, items))
#print(squared)

#filtered_list = list(filter(lambda x: zipping(x), zipped_files))
#print(filtered_list)
'''

a = []
for root, directories, files in os.walk('H:/Documents/work'):
	for filename in files:
		a.append(filename)
print(a)

b = []
#testing: concatenating filenames from separate list to a root dir and then adding those dir to a list
for root,directories,files in os.walk('H:/Documents/work'):
	for filename in a:
		b.append(os.path.join(root,filename))
print(b)



'''

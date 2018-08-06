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
dict1={'txt0':0,'txt1':1,'txt2':2}
dict2={'txt0':0,'txt2':2}


#print('txt3' in dict1)

def compare_delete(dict1,dict2):
	to_delete = []
	for key in dict1:
		if key not in dict2:
			continue
		elif dict1[key]==dict2[key]:
			to_delete.append(key)

	
	return to_delete


print(compare_delete(dict1,dict2))
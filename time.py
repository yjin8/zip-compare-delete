from datetime import datetime
import time

#d = datetime.date.today()
#print(d)
'''
t = time.time()
old_time = t - 2592000

print(t)

t = datetime.fromtimestamp(old_time)
print(t)
print(t.month)
print(t.year)
'''

def get_year_month():
	current_time = time.time()
	month_earlier = current_time - 2592000 
	t = datetime.fromtimestamp(month_earlier)
	YEAR_MONTH = "{}-{:02d}".format(t.year, t.month)
	return YEAR_MONTH

print(get_year_month())
#!/usr/bin/env python
from matplotlib import pyplot as plt
import numpy as np

# f = open("C:\\Users\\wondering\\Desktop\\lab-Semester5\\week1Arkadiy\\im_stats") #opening the file to parse
f=open("C:\\Users/wondering/Desktop/lab-Semester5/haotian_isis_full_data.txt")
content = f.read() #reading the contents
line_split = content.split('\n') #splitting into a line-by-line matrix

mean_values = []
scatter_values = []
name_aban=[]
i=0
for line in line_split: #reading line by line
	#space_split[0] - mean:
	#space_split[1] - mean value
	#space_split[2] - scatter:
	#space_split[3] - scatter value
	i=i+1
	space_split = line.split(' ')

	if space_split != ['']: #to make sure it won't care about empty lines
		if(float(space_split[1])>50):
			print(i)
			continue
		if(float(space_split[3])>50):
    			continue
		
		mean_values.append(float(space_split[1]))
		scatter_values.append(float(space_split[3]))
total_NUM=len(mean_values)
print('haotian')
print('mean values: ',sum(mean_values)/total_NUM)
print('scatter values: ',sum(scatter_values)/total_NUM)
plt.subplot(2,2,1)
plt.hist(mean_values,log=True)
plt.title('mean')
plt.subplot(2,2,2)
plt.title('scatter')
plt.hist(scatter_values,log=True)


f=open("C:\\Users/wondering/Desktop/lab-Semester5/haotian_isis_full_data.txt")
content = f.read() #reading the contents
line_split = content.split('\n') #splitting into a line-by-line matrix

mean_values = []
scatter_values = []

for line in line_split: #reading line by line
	#space_split[0] - mean:
	#space_split[1] - mean value
	#space_split[2] - scatter:
	#space_split[3] - scatter value

	space_split = line.split(' ')
	if(float(space_split[1])>50):
    			continue
	if(float(space_split[3])>50):
    			continue
	if space_split != ['']: #to make sure it won't care about empty lines

		mean_values.append(float(space_split[1]))
		scatter_values.append(float(space_split[3]))
total_NUM=len(mean_values)
print('arkadiy')
print('mean values: ',sum(mean_values)/total_NUM)
print('scatter values: ',sum(scatter_values)/total_NUM)
plt.subplot(2,2,3)
plt.hist(mean_values,log=True)
plt.title('mean')
plt.subplot(2,2,4)
plt.hist(scatter_values,log=True)
plt.title('scatter')

plt.show()

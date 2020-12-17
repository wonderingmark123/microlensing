
from matplotlib import pyplot as plt
import numpy as np

# f = open("C:\\Users\\wondering\\Desktop\\lab-Semester5\\week1Arkadiy\\im_stats") #opening the file to parse
f=open("C:\\Users/wondering/Desktop/lab-Semester5/week1Arkadiy/im_stats.txt")
content = f.read() #reading the contents
line_split = content.split('\n') #splitting into a line-by-line matrix

seeing_values = []
airmass_values = []
background_values = []
name=[]
for line in line_split: #reading line by line
	#space_split[0] - name
	#space_split[1] - seeing=
	#space_split[2] - seeing VALUE
	#space_split[3] - airmass=
	#space_split[4] - airmass VALUE
	#space_split[5] - background=
	#space_split[6] - background VALUE

	space_split = line.split(' ')

	if space_split != ['']: #to make sure it won't care about empty lines
		if float(space_split[6])>1300:
			continue
		if float(space_split[2])>20:
				continue
		if float(space_split[2])<0:
			continue
		if float(space_split[4])>2:
				continue
		# if float(space_split[6])>1500:
    	# 		continue
		# if float(space_split[6])<1000:
    	# 		continue
		name.append(space_split[0])
		seeing_values.append(float(space_split[2]))
		airmass_values.append(float(space_split[4]))
		background_values.append(float(space_split[6]))
print(np.max(airmass_values))
print(np.min(airmass_values))
print(np.min(seeing_values))
print(np.max(seeing_values))

seeing_norm=seeing_values/np.max(seeing_values)
airmass_norm=airmass_values/np.max(airmass_values)
background_norm=background_values/np.max(background_values)
FINAL=np.array( airmass_norm + seeing_norm)
# FINAl=seeing_values + airmass_values + background_values
limit=1.25
length = len(seeing_values)
images = np.arange(0, length, 1)
# print(FINAL)
seeing_reference=[]
background_ref=[]
airmass_ref=[]

for i in range(1,length) :
	if FINAL[i] < limit :
		print(i,name[i][53:],'seeing value:',seeing_values[i],'background: ',background_values[i],'airmass value:',airmass_values[i],'SUM:',FINAL[i])
		seeing_reference.append(float(seeing_values[i]))
		background_ref.append(float(background_values[i]))
		airmass_ref.append(float(airmass_values[i]))

fig = plt.figure(1, figsize = (10, 8))
data = fig.add_subplot(311)
data.tick_params(labelsize=15)
data.hist(seeing_values)
data = fig.add_subplot(312)
data.hist(background_values)
data = fig.add_subplot(313)

data.hist(airmass_values)
# data.set_xlabel('Images', size = 20)
# data.set_ylabel('Quantity', size = 20)

# print(np.find(FINAL<0.75))
# data.plot(images, seeing_values, label = 'Seeing')
# data.plot(images, airmass_values, label = 'Airmass')
# data.plot(images, background_values, label = 'Background light')
# data.plot(images, FINAl, label = 'FINAL')
data.legend(loc='upper right', shadow=False, fontsize='15')
plt.show()

import matplotlib.pyplot as plt
import csv
import glob, os, os.path

fig, ax = plt.subplots() 
sheep_files = glob.glob('sheep*')
dog_files = glob.glob('dogs*')



for s in sheep_files:    
    x = []
    y = []
    
    with open(s,'r') as csvfile:
        lines = csv.reader(csvfile, delimiter=',')
        for row in lines:
            x.append(float(row[0]))
            y.append(float(row[1]))

    ax.plot(x, y)
for d in dog_files:    
    x = []
    y = []
    
    with open(d,'r') as csvfile:
        lines = csv.reader(csvfile, delimiter=',')
        for row in lines:
            x.append(float(row[0]))
            y.append(float(row[1]))

    ax.plot(x, y, linestyle='dashed')

ax.set_xlim([-12, 12])  
ax.set_ylim([-12, 12])
plt.grid()  
plt.show()
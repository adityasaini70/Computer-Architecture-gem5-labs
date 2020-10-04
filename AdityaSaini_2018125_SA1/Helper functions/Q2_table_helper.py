#CA Assignment 1 - Q2 table helper function
#Function : Makes different combinations of associations & cache size and passes them onto the config file(Q1.py) for analysis
#Name - Aditya Saini
#Roll number - 2018125
#Branch - B.Tech ECE

import os
import subprocess
import shlex

#Defining the different associations and cache sizes
l2_cache_assoc = [1,2,4,8]
l2_cache_size = ['4kB','8kB','16kB','32kB','64kB','256kB','512kB','1024kB']

#table containing different values of miss rates for different memory sizes and associations in form of a dictionary
table={}

for i in l2_cache_size:
    table[i]={}
    for j in l2_cache_assoc:
        print(i,j)

        #Passing different arguments to the config file(Q1.py)
        command = '/home/metronomous/gem5/build/X86/gem5.opt /home/metronomous/gem5/College/Assignment1/Q1.py  --l2_size '+i+' --l2_assoc '+str(j)
        process=subprocess.Popen(shlex.split(command), cwd = "/home/metronomous/gem5", stdout=subprocess.PIPE)
        output, error = process.communicate()

        #Extracting the output values 
        second_process=subprocess.Popen('grep l2cache stats.txt'.split(),cwd= '/home/metronomous/gem5/m5out/', stdout=subprocess.PIPE)
        output, error = second_process.communicate()
        output = [val.split() for val in str(output).split('\\n')]
        
        #Extracting values which are concerned only with miss_rates
        temp=[]
        for k in output:
            if 'miss_rate' in k[0]:
                temp.append(k)
                #print(k)
        table[i][j]=temp

#Storing the table in a file for further analysis
with open('table.txt', 'w') as f:
	print(table, file=f)

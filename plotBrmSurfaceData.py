# -*- coding: utf-8 -*-
"""
Created on Mon May 30 16:10:24 2016

Script to plot surface data from the BIRM

@author: dconrad

Last Edit:

Last Edit Date:
"""

import matplotlib.pyplot as plt
import numpy as np
import datetime
from matplotlib import dates as md
import scipy
import pandas as pd
import matplotlib

filename = '/rhome/dconrad/Desktop/QLCS_Tor_Cases/Albertville_20150104/MIPS/brm_20150104_sfc_Short.dat'

#Import data
data = np.loadtxt(filename, delimiter = ',')

year = data[:,1]
day = data[:,2]
hourMin = data[:,3]
sec = data[:,4]
pres = data[:,5]
temp2m = data[:,6]
relHum = data[:,7]
temp10m = data[:,8]
windSpeed = data[:,9]
windDir = data[:,10]
#rainRate = data[:,11]
#solarRad = data[:,12]
temp1m = data[:,13]
tempHalfm = data[:,14]

# Create Gregorian date
date = datetime.datetime(int(year[0]),1,1) + datetime.timedelta(day[0]-1)
gdate = date.strftime('%m/%d/%Y') #With /s
tdate = date.strftime('%m%d%Y') #Without /s

#Create hour and minute array
#Use splicing of hourMin array to fill separate arrays
hour = [0]*len(hourMin)
minute = [0]*len(hourMin)

for i in range(0, len(hourMin)):
    string = '%04d'%hourMin[i] #Create 4 digit string
    hour[i] = int(string[0:2]) #First two numbers are hour
    minute[i] = int(string[2:4]) #2nd two numbers are minute

x=[]
date_dummy=[]
dates=[]
for i in range(0,len(hourMin)):
    x.append(str(hour[i])+':'+str(minute[i]))

for j in range(0,len(x)):
   date_dummy.append(datetime.datetime.strptime(x[j], "%H:%M"))

for k in range(0,len(x)):
   dates.append(matplotlib.dates.date2num(date_dummy[k]))

#plt.subplot(121)
xfmt = md.DateFormatter('%H:%M')
plt.plot_date(dates,pres,'b-')
ax=plt.gca()
ax.xaxis.set_major_formatter(xfmt)
ax.xaxis_date()
ax.set_xlabel('Time (UTC)')
plt.title(gdate + " Pressure Trace")
plt.ylabel("Station Pressure [mb]")

plt.savefig("pressure.png", dpi = 250)


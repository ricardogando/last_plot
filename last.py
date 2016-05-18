
import os
import sys
import time
from pylab import *

try:
    user = sys.argv[1]
    print user
except Exception,e:
    print e
    user = '' 

exehour = int(time.time())

#times = open('last.txt','r').readlines()
times = os.popen('last '+user).readlines()
times.remove(times[-1])
times.remove(times[-1])

timein = []
timeout = []
for time in times:
    try:
        ttimein = time.split()[6]
        ttimein = float(ttimein.split(':')[0])+float(ttimein.split(':')[1])/60.
        timein.append(ttimein)
        if 'logged' not in time:
            ttimeout = time.split()[8]
            ttimeout = float(ttimeout.split(':')[0])+float(ttimeout.split(':')[1])/60.
            timeout.append(ttimeout)
    except Exception,e:
        print e

print
print timein
print
print timeout
print

figure(1)
bins = arange(0,25,1)
hist(timein, bins=bins, histtype='step',label='start', align='left')
hist(timeout, bins=bins, histtype='step',label='end', align='left')
xticks(bins)
xlim(0,24)
yl,yu = ylim()
ylim(ymax=1.1*yu)
xlabel('time')
ylabel('N')
legend()
savefig('last'+str(exehour)+user+'.png')


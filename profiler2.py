# logger2.py
# An example that shows the application possibilities of https://github.com/hilch/Pvi.py
#
# extract all profiler data from a systemdump container
#

import tarfile
import tempfile
import os
import re
from pvi.utils import BrProfilerDataFile

pattern = re.compile(r'(BuR_SDM_profiling_.*pd)')

#systemdump = r'C:\Temp\BuR_SDM_Sysdump_2023-07-31_11-11-41.tar.gz'
systemdump = r'C:\Temp\BuR_SDM_Sysdump_2023-07-25_10-35-25.tar.gz'

with tempfile.TemporaryDirectory() as t:
    tf = tarfile.open( systemdump, mode = 'r')
    tf.extractall(t)
    dataDirName = t + '/Data Files'
    dataFileNames = os.listdir(dataDirName)
    for dataFileName in dataFileNames:
        match = pattern.findall(dataFileName)
        if match:
            profilingName = match[0]
            try:
                profilerData = BrProfilerDataFile(dataDirName + '/' + dataFileName)
            except TypeError: # ingore all non-profiler files
                continue  

            print(profilerData.objects)

            #print( profilerData.info )

            #print(profilerData.taskClasses)

            entries = profilerData.entries     
            #print( entries[0], entries[4999] )   





# profiler2.py
# An example that shows the application possibilities of https://github.com/hilch/Pvi.py
#
# extract all profiler data from a systemdump container and save it to csv
# a separate *.txt file is created with object information
#

import tarfile
import tempfile
import csv
import os
import re
import locale
from pprint import PrettyPrinter
from pvi.utils import BrProfilerDataFile

locale.setlocale(locale.LC_ALL, '')

pattern = re.compile(r'(BuR_SDM_profiling_.*pd)')

systemdump = r'C:\Temp\BuR_SDM_Sysdump_2023-07-31_11-11-41.tar.gz'

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

            with open(f'{dataFileName}.txt', 'w', newline = '') as f: 
                pp = PrettyPrinter( indent = 4, stream = f )
                print( dataFileName,  '\n\nSummary:\n', file = f)
                pp.pprint( profilerData.info )
                print( '\n\ntask classes:\n', file = f )
                pp.pprint( profilerData.taskClasses )                
                print( '\n\ncyclic tasks:\n', file = f )
                pp.pprint( profilerData.cyclicTasks )                
                print( '\n\nsystem tasks:\n', file = f )
                pp.pprint( profilerData.systemTasks )                
                print( '\n\ninterrupt handler:\n', file = f )
                pp.pprint( profilerData.interruptHandler )                
                print( '\n\nprofiled library functions:\n', file = f )
                pp.pprint( profilerData.libraryFunctions )                 
                
                
            with open(f'{dataFileName}.csv', 'w', newline = '') as f: 
                writer = csv.writer(f, delimiter= ';', quotechar="'" )
                writer.writerow ( ["Nr", "time", "object name", "ident","event", "event description"])            
                for n, e in enumerate(profilerData.entries):
                    writer.writerow( ( n+1, locale.format_string( '%.6f', e.microseconds), e.objectName, hex(e.objectIdent), hex(e.event), e.eventDescription ) ) 





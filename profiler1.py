
# profiler1.py
# An example that shows the application possibilities of https://github.com/hilch/Pvi.py
#
# extract all profiler data from a *.pd file and save it to csv
# a separate *.txt file is created with object information
#

import csv
import locale
from pprint import PrettyPrinter
from pvi.utils import BrProfilerDataFile

folder = r'C:\Temp\BuR_SDM_Sysdump_2023-07-25_10-35-25.tar\BuR_SDM_Sysdump_2023-07-25_10-35-25\Data Files'
file = r'BuR_SDM_profiling_2023-07-25_09-04-41.pd'

profilerData = BrProfilerDataFile(folder + '\\' + file)

with open(f'{file}.txt', 'w', newline = '') as f: 
    pp = PrettyPrinter( indent = 4, stream = f )
    print( file,  '\n\nSummary:\n', file = f)
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


    
with open(f'{file}.csv', 'w', newline = '') as f: 
    writer = csv.writer(f, delimiter= ';', quotechar="'" )
    writer.writerow ( ["Nr", "time", "object name", "ident","event", "event description"])            
    for n, e in enumerate(profilerData.entries):
        writer.writerow( ( n+1, locale.format_string( '%.6f', e.microseconds), e.objectName, hex(e.objectIdent), hex(e.event), e.eventDescription ) ) 


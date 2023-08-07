from pathlib import Path
import sys

pviPath = str(Path(__file__).parents[1])
cwd = str(Path(__file__).parents[0])

sys.path.append( pviPath )

import hashlib
from pvi.utils import BrProfilerDataFile

for f, c in {'profiler1.pd' : '9b1e4d7c33dd77f59f429e6d706513c5e098a1fe225e4be54a08a203929e1baa', 
             'profiler2.pd' : 'c391110f1e8b9c7e8163e657049e7611d8c7128901076bd241ba841bd96a1b67', 
             'profiler3.pd' : '65cc7563e35b30a1e242633175749ef050115375b8e59f3887b4ede1a06ae189'
             }.items():

    profilerData = BrProfilerDataFile( cwd + '\\' + f)

    result = str( profilerData.taskClasses ) + str( profilerData.cyclicTasks) + str( profilerData.systemTasks) + \
            str( profilerData.interruptHandler) + str( profilerData.libraryFunctions) 
    h = hashlib.sha256( result.encode() )

    if h.hexdigest() == c:
        print(f, "pass !")
    else:
        print(f, "failed !")


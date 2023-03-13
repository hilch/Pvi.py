# logger2.py
# An example that shows the application possibilities of https://github.com/hilch/Pvi.py
#
# PLC counterpart is B&R's 'coffee machine' running on ArSim 
# as provided with Automation Studio 4.1.17.113 (which
# can be downloaded free of charge from https://www.br-automation.com)
#
# extract all logger from a systemdump container and save them as csv.
#

import tarfile
import tempfile
import os
import csv
import re
from pvi.utils import BrLoggerFile

pattern = re.compile(r'(BuR_SDM_([a-z0-9]*)_.*br)')

systemdump = r'C:\Temp\BuR_SDM_Sysdump_2023-03-13_14-39-29.tar.gz'

with tempfile.TemporaryDirectory() as t:
    tf = tarfile.open( systemdump, mode = 'r')
    tf.extractall(t)
    dataDirName = t + '/Data Files'
    dataFileNames = os.listdir(dataDirName)
    for dataFileName in dataFileNames:
        match = pattern.findall(dataFileName)
        if match:
            loggerName = match[0][1]
            try:
                logger = BrLoggerFile(dataDirName + '/' + dataFileName)
            except TypeError: # ingore all non-logger files
                continue                
            entries = logger.entries
            with open(f'{loggerName}.csv', 'w', newline = '') as f: 
                writer = csv.writer(f, dialect='excel')
                writer.writerow ( ["RecordID", "Time", "Severity", "Code", "EventID", "OriginID", "ObjectID", "AsciiData", "BinaryData"])            
                for e in entries:
                    writer.writerow( (e.RecordID, e.Time, e.Severity, e.Code, e.EventID, e.OriginID, e.ObjectID, e.AsciiData, e.BinaryData) )




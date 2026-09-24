# modules3.py
# An example that shows the application possibilities of https://github.com/hilch/Pvi.py
#
# in this exammple we search for BR files (*.br) in a folder and read the type their content
#

import os
from pvi.utils import BrFile, ModuleType, BrDataObjectFile, BrMotionDataObjectFile, BrXMLBasedConfigFile

# 'Temp' folder contains 'anonymous' file names and makes it difficult to determine the content
# or alternatively take a view into the 'Binaries' folder of a project
path_of_the_directory = r'C:\projects\CoffeeMachine\Temp\Simulation\Simulation\ARsim\RPSHD\USERROM'

ext = ('.br')
filenames = [f for f in os.listdir(path_of_the_directory) if f.endswith(ext)]

for filename in filenames:
    module = BrFile(path_of_the_directory + '\\' + filename)
    print( f'type of {filename} is {module.fileType.name}', end='' )
    # let's check what's inside some modules
    if module.fileType == ModuleType.DATA_OBJECT:
        data_module = BrDataObjectFile(path_of_the_directory + '\\' + filename)
        data = data_module.data
        print( f", data: {data[:20]} .... {data[-20:]}")
    elif module.fileType == ModuleType.MOTION_DATA_OBJECT:
        data_module = BrMotionDataObjectFile(path_of_the_directory + '\\' + filename)
        data = data_module.data
        print( f", data: {data[:20]} .... {data[-20:]}")
    elif module.fileType == ModuleType.XML_BASED_CONFIGURATION:
        data_module = BrXMLBasedConfigFile(path_of_the_directory + '\\' + filename)
        data = str.replace( data_module.data, '\r\n', '')
        print( f", data: {data[:20]} .... {data[-20:]}")
    else:
        print("")
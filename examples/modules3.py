# modules.py
# An example that shows the application possibilities of https://github.com/hilch/Pvi.py
#
# in this exammple we search for BR files (*.br) in a folder and read the type their content
#

import os
from pvi.utils import BrFile

# 'Temp' folder contains 'anonymous' file names and makes it difficult to determine the content
path_of_the_directory = r'C:\projects\CoffeeMachine\Temp\Simulation\Simulation\ARsim\RPSHD\USERROM'

ext = ('.br')
filenames = [f for f in os.listdir(path_of_the_directory) if f.endswith(ext)]

for filename in filenames:
    module = BrFile(path_of_the_directory + '\\' + filename)
    print( f'content of {filename} is {module.fileType}' )

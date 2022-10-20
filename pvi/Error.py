#
# Pvi.py
# Python connector for B&R Pvi (process visualization interface)
#
#  https://github.com/hilch/Pvi.py
# Permission is hereby granted, free of charge, 
# to any person obtaining a copy of this software and associated documentation files (the "Software"), 
# to deal in the Software without restriction, 
# including without limitation the rights to use, copy, modify, merge, publish, distribute, 
# sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, 
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included 
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, 
# INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. 
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, 
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, 
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
    
class PviError(Exception):
    _messages = {   
      4000: 'Error from coding function (_CPinfo)',
      4001: 'Error from decoding function (_CPinfo)',
      4002: 'Unexpected telegram (_CPinfo)',
      4003: 'Default error (_CPinfo)',
      4010: 'Error from coding function (_CPreset)',
      4011: 'Error from decoding function (_CPreset)',
      4012: 'Unexpected telegram (_CPreset)',
      4013: 'Default error (_CPreset)',
      4014: 'Incorrect password (_CPreset)',
      4020: 'Error from coding function (_CPclearMem)',
      4021: 'Error from decoding function (_CPclearMem)',
      4022: 'Unexpected telegram (_CPclearMem)',
      4023: 'Default error (_CPclearMem)',
      4024: 'Cannot find or clear memory type (_CPclearMem)',
      4025: 'PLC must be in diagnostic mode (_CPclearMem)',
      4030: 'Error from coding function (_CPmemInfo)',
      4031: 'Error from decoding function (_CPmemInfo)',
      4032: 'Unexpected telegram (_CPmemInfo)',
      4033: 'Default error (_CPmemInfo)',
      4040: 'Error from coding function (CPmemInfo)',
      4041: 'Error from decoding function (CPmemInfo)',
      4042: 'Unexpected telegram (CPmemInfo)',
      4043: 'Default error (CPmemInfo)',
      4044: 'Object does not exist (CPmemInfo)',
      4050: 'Error from coding function (_DeleteModule)',
      4051: 'Error from decoding function (_DeleteModule)',
      4052: 'Unexpected telegram (_DeleteModule)',
      4053: 'Default error (_DeleteModule)',
      4054: 'Object does not exist (_DeleteModule)',
      4055: 'PI must be stopped (_DeleteModule)',
      4056: 'Object cannot be uninstalled (_DeleteModule)',
      4057: 'Object cannot be deleted because it is used in a task (_DeleteModule).',
      4060: 'Error from coding function (_DownloadModule)',
      4061: 'Error from decoding function (_DownloadModule)',
      4062: 'Unexpected telegram (_DownloadModule)',
      4063: 'Default error (_DownloadModule)',
      4064: 'Download aborted by USER (_DownloadModule)',
      4065: 'Download blocked for USER (_DownloadModule)',
      4066: 'No free entries in the module table (_DownloadModule)',
      4067: 'Not a BR module (2b97) (_DownloadModule)'
            '\nThe specified module for the download is not a BR module.'
            '\nIt is not possible to transfer other file types by changing their'
            '\nextension to .br.',
      4068: 'Damaged BR module checksum (_DownloadModule)',
      4069: 'BR module installation error (_DownloadModule)'
            '\nThe module to be transferred could not be installed.'
            '\nThe reason for this could be an incorrect download sequence if,'
            '\nfor example, a library whose function is required in the transferred '
            '\nmodule has not yet been installed.',
      4070: 'Incorrect length of BR module (_DownloadModule)',
      4071: 'Insufficient target memory (_DownloadModule)',
      4072: 'Error while burning the BR module (_DownloadModule)',
      4073: 'NC Manager not installed (_DownloadModule)',
      4074: 'Error from NC Manager DL function (_DownloadModule)',
      4080: 'Error from encoding function (_UploadModule)',
      4081: 'Error from decoding function (_UploadModule)',
      4082: 'Unexpected telegram (_UploadModule)',
      4083: 'Default error (_UploadModule)',
      4084: 'Upload aborted by USER (_UploadModule)',
      4085: 'Module cannot be found (incorrect name) (_UploadModule)',
      4086: 'Module status not equal to READY (_UploadModule)',
      4087: 'Upload of module blocked (_UploadModule)',
      4088: 'Upload blocked for USER (_UploadModule)',
      4104: 'TC already running (_TKresume)',
      4105: 'TC not found (_TKresume)',
      4114: 'TC already stopped (_TKsuspend)',
      4115: 'TC not found (_TKsuspend)',
      4124: 'Task already running (_TaskResume)',
      4125: 'Task not found (_TaskResume)',
      4134: 'Task already stopped (_TaskSuspend)',
      4135: 'Task not found (_TaskSuspend)',
      4144: 'Task not found (_TaskSetStepcount)',
      4174: 'Invalid PV ID (_ReadVars)',
      4175: 'PV not found (_ReadVars)',
      4176: 'Incorrect PV length (_ReadVars)',
      4177: 'Dyn. PV not used (NULL pointer) (_ReadVars)',
      4184: 'Invalid PV ID (_WriteVar)',
      4185: 'PV not found (_WriteVar)',
      4186: 'Incorrect PV length (_WriteVar)',
      4187: 'Dyn. PV not used (NULL pointer) (_WriteVar)',
      4194: 'Invalid PV ID (data type, base ptr., etc.) (_ForceVarOn)',
      4195: 'Invalid task class (_ForceVarOn)',
      4196: 'No available entry in force table (_ForceVarOn)',
      4204: 'Invalid PV ID (data type, base ptr., et.) (_ForceVarOff)',
      4205: 'Invalid task class (_ForceVarOff)',
      4206: 'PV not forced (_ForceVarOff)',
      4224: 'Diagnostic task not loaded (_DiagListModules)',
      4234: 'Diagnostic task not loaded (_DiagDeleteModule)',
      4235: 'DIAG module index invalid, list not yet read? (_DiagDeleteModule)',
      4244: 'Diagnostic task not loaded (_DiagExit)',
      4264: 'No HWC determination performed on PLC (e.g. in diag. mode) (_ListHwComponets)',
      4283: 'Invalid time format for access function POBJ_ACC_DATE_TIME',
      4334: 'Maximum number of event masters reached',
      4354: 'Invalid server object ID (_LinkEventVars)',
      4355: 'PV not found (_LinkEventVars)',
      4356: 'Incorrect Commserv version (_LinkEventVars)',
      4366: 'Incorrect Commserv version (_UnlinkEventVars)',
      4405: 'Link node not found on PLC (_LNIdentify)',
      4464: 'Log entry not found in BR log data module (_LogDataIdentify)',
      4475: 'PLC denying access to BR log data module (_LogDataClear)',
      4484: 'Memory error on PLC (_LogDataRead)',
      4485: 'Damaged data in BR log data module (_LogDataRead)',
      4486: 'Unknown data format in BR log data module (_LogDataRead)',
      4525: 'Specified library not found (_LibraryList)',
      4599: 'Link nodes not supported on PLC operating system',
      4604: 'Illegal syntax in routing path information',
      4801: 'Error setting up memory',
      4802: 'Invalid object type',
      4803: 'Service not supported',
      4804: 'Object property not defined'
            '\nAn object property required by the INA2000 line (e.g. connection description)'
            '\nis not defined.',
      4805: 'Incorrect service status',
      4806: 'Invalid object information'
            '\nThe object (variable) cannot be identified on the controller.'
            '\nThe reason could be an incorrect connection description (CD parameter)'
            '\nor an invalid object hierarchy'
            '\n(e.g. local variable registered on CPU object).'
            '\nWhen PVI applications access a controller running AR 3.00 (SG4) / AR 2.30 (SGC)'
            '\nor later via the INA2000 line with a PVI version lower than V3.0.0,'
            '\nerror 4813 is reported for all global variables and '
            '\nerror 4806 for all local variables.',
      4807: 'Invalid object hierarchy'
            '\nA PVI object was registered at an invalid position in the object hierarchy.',
      4808: 'No connection to PLC available'
            '\nNo connection can be established with the PLC using the specified connection'
            '\nparameters (station number, IP address, etc.), '
            '\nor the connection to the controller was interrupted.'
            '\nIf the problem occurs the first time a connection is established,'
            '\ncheck the connection parameters.'
            '\nWith an unstable&quot; connection, increasing parameter /RT (response timeout)'
            '\nmay solve the problem.'
            '\nHowever, a higher /RT also increases the time it takes to detect'
            '\nconnection errors.',
      4809: 'Cannot install connection to PLC',
      4810: 'Service not executable',
      4811: 'Service active',
      4812: 'Service error response',
      4813: 'Identification error'
            '\nThe object (task, module, variable) cannot be identified on the controller.'
            '\nThe reason could be an incorrect connection description (CD parameter)'
            '\nor an invalid object hierarchy'
            '\n(e.g. local variable registered on CPU object).'
            '\nWhen PVI applications access a controller running AR 3.00 (SG4) / AR 2.30 (SGC)'
            '\nor later via the INA2000'
            '\nline with a PVI version lower than V3.0.0, error 4813 is reported for'
            '\nall global variables and error 4806 for all local variables.',
      4814: 'Error reading variable',
      4815: 'Service currently not implemented',
      4816: 'Error reading variable list',
      4817: 'Error reading module list',
      4818: 'Error reading PLC info',
      4819: 'Service aborted'
            '\nA running user function (e.g. PviReadRequest, PviWriteRequest) was aborted'
            '\nby another function (e.g. PviUnlink, PviDelete).',
      4820: 'Error reading BR module'
            '\nCase A): A BR module with illegal data was transferred'
            '\n         or read by the controller.'
            '\nCase B): The corresponding task was stopped on the controller'
            '\n         or the task module was overloaded.'
            '\nCase C): Syntax error in the filename of a BR module'
            '\n        (e.g. for access type POBJ_ACC_DOWNLOAD or POBJ_ACC_UPLOAD.'
            '\n        It is possible that the filename is not delimited by apostrophes.',
      4821: 'Cannot write variable data.'
            '\nWrite access is not permitted to constants'
            '\nor pointer values of dynamic variables.',
      4823: 'Internal error in connection with the INA2000 protocol',
      4824: 'Event mode not possible for structure or array variable or link node variable'
            '\nCase A): An attempt was made to register a structure or an array as an'
            '\nevent variable (PLC event variable).'
            '\nHowever, only basic data types are permitted for event operation under INA2000.'
            '\nCase B): An attempt was made to register a link node variable as an'
            '\nevent variable (PLC event variable).'
            '\nSolution: Attribute &quot;e&quot;'
            '\nmust be removed from variable object parameter /AT.',
      4825: ' Unknown format of PV section.'
            '\nThe PV information stored in the addressed BR module cannot be interpreted'
            '\nby the PVI version used.'
            '\nSolution: Use a newer PVI version.', 
      4830: 'Invalid application module name.'
            '\nThe specified application module name is invalid or is not within'
            '\nthe defined scope.'
            '\nSolution: Check CPU object parameter /AM.',
      4901: 'ICOMM DLL not found',
      4902: 'ICOMM DLL invalid',
      4903: 'Internal error (APLCIF)',
      4904: 'Invalid offset',
      4905: 'Error establishing connection (connection already established)',        
      11001: 'Internal ANSL error.'
            '\nAn internal error has occurred in the ANSL line'
            '\nor in the ANSL communication layer.'
            '\nThe PVI logger output (component PviMan.exe/LnAnsl.dll'
            '\nand PviMan.exe/LnAnsl.dll/ANSL)'
            '\ncan be used to further analyze the problem.',
      11002: 'ANSL version conflict.'
            '\nThe version of the ANSL communication layer or AR ANSL online server used by'
            '\nthe ANSL line is not compatible.'
            '\nSolution: Use a newer version of Automation Runtime or PVI.',
      11003: 'ANSL protocol error.'
            '\nThe ANSL communication layer has received invalid protocol data from the'
            '\nAR ANSL online server.'
            '\nThe PVI logger output (component PviMan.exe/LnAnsl.dll/ANSL) can be used'
            '\nto further analyze the problem.',
      11004: 'ANSL object error.'
            '\nThe object state in the ANSL communication layer or in the AR ANSL online'
            '\nserver is invalid.'
            '\nThe PVI logger output (component PviMan.exe/LnAnsl.dll/ANSL) can be used'
            '\nto further analyze the problem.',
      11005: 'Undefined ANSL error message received.'
            '\nAn error message received from the AR ANSL server cannot be interpreted.'
            '\nFor the ANSL error code, see the PVI logger output'
            '\n(component PviMan.exe/LnAnsl.dll).'
            '\nSolution: Use a newer PVI version.',
      11006: 'Invalid response data received.'
            '\nThe response data received from the AR ANSL online server is invalid.'
            '\nThe PVI logger output (component PviMan.exe/LnAnsl.dll/ANSL) can be used'
            '\nto further analyze the problem.',
      11007: 'Entry in XML response data not found or invalid.'
            '\nAn entry (tag or attribute) could not be found when evaluating the XML'
            '\nresponse data from the AR ANSL online server'
            '\nor the entry contains invalid data. The cause may be a version conflict.',
      11009: 'BrMod104 error occurred.'
            '\nAn error has occurred in connection with component BrMod104.'
            '\nThe cause may be a version conflict.'
            '\nThe PVI logger output (component PviMan.exe/LnAnsl.dll) can be used'
            '\nto further analyze the problem.',
      11010: 'Invalid device name.'
            '\nThe device name specified in the connection description of the PVI device'
            '\nobject is invalid or the device is not supported by the ANSL line.'
            '\nSolution: The connection description of the device object must specify'
            '\n/IF=TcpIp.',
      11011: 'Invalid application module name.'
            '\nThe specified application module name is invalid'
            '\nor is not within the defined scope.'
            '\nSolution: Check CPU object parameter /AM.',
      11012: 'Invalid data format.'
            '\nThe AR ANSL online server supplied an invalid variable data format'
            '\nor an incorrect data length.'
            '\nThe cause may be an error in the online server.'
            '\nThe PVI logger output (component PviMan.exe/LnAnsl.dll/ANSL) can be used'
            '\nto further analyze the problem.',
      11013: 'Unknown format of PV section.'
            '\nThe PV information stored in the addressed BR module cannot be interpreted'
            '\nby the PVI version used.'
            '\nSolution: Use a newer PVI version.',
      11014: 'Event mode not possible for link node variable.'
            '\nAn attempt was made to register a link node variable as an ANSL event variable'
            '\n(PLC event variable).'
            '\nSolution: Remove attribute e from variable object parameter AT.',
      11020: 'Unable to establish ANSL communication connection.'
            '\nCase A) Unable to establish communication connection to ANSL online server'
            '\nwith specified connection parameters.'
            '\nSolution: Check the connection parameters in the connection description'
            '\nof the CPU object, PLC and network functionality.'
            '\nCase B) Network layer (Windows) reports system error.'
            '\nThe PVI logger output (component PviMan.exe/LnAnsl.dll/Communication)'
            '\ncan be used to further analyze the problem.',
      11021: 'ANSL communication timeout.'
            '\nThe ANSL communication connection was aborted on the PVI side (client)'
            '\ndue to a timeout error.'
            '\nCause: No life monitoring signals or other data could be received'
            '\nwithin the specified timeout.'
            '\nSolution: Check PLC and network functionality.'
            '\nIf necessary, increase the timeout parameter (see CPU object parameter /COMT).',
      11022: 'ANSL communication connection aborted.'
            '\nCase A) The ANSL communication connection was aborted on the PLC side'
            '\n(AR ANSL online server).'
            '\nThe cause must be analyzed on the PLC (e.g. AR log file).'
            '\nA timeout error may have occurred on the PLC side or the connection'
            '\nmay have been closed after a fatal error.'
            '\nCase B) The ANSL communication connection was aborted by the network layer.'
            '\nThe PVI logger output (component PviMan.exe/LnAnsl.dll/Communication)'
            '\ncan be used to further analyze the problem.',
      11023: 'Hostname not found.'
            '\nNo IP address could be identified for the specified hostname.'
            '\nSolution: Check connection parameter /IP in the connection description'
            '\nof the CPU object. Check DNS functionality.',
      11024: 'Error opening or reading SSL/TLS configuration file.'
            '\nThe specified SSL/TLS configuration file (PVI parameter /TLS) cannot be opened'
            '\nor contains invalid data or directory paths.',
      11030: 'Request aborted.'
            '\nAn ANSL service request was aborted by an action of the PVI application,'
            '\nby an ANSL communication failure or by the AR ANSL online server.',
      11031: 'Object or service not supported in ANSL.'
            '\nThe ANSL object type or ANSL service request is not supported by the'
            '\nAR ANSL online server.'
            '\nSolution: Check the parameters of the access mode used.'
            '\nIf the parameters are valid (see PVI help documentation),'
            '\nthe service may not yet be supported by the AR ANSL online server used.'
            '\nIn this case you have to switch to a newer AR version.',
      11032: 'Invalid service parameters.'
            '\nOne or more service parameters of the access mode are invalid.'
            '\nSolution: Check the service parameters.',
      11033: 'Object not found.'
            '\nThe specified module, task or variable object cannot be found on the PLC.'
            '\nSolution: Check the connection description.',
      11035: 'Object not ready.'
            '\nThe AR ANSL online server has set the status not ready'
            '\nfor the addressed ANSL object.'
            '\nThe status indicates that the object is temporarily unable to process services.'
            '\nThis status can occur, for example, after downloading a task for'
            '\nall variable objects assigned to the task.',
      11040: 'Invalid internal module list.'
            '\nThe module list used by the ANSL line is not valid.'
            '\nCause: Faulty data was read from the ANSL online server'
            '\n(PV section or task information).'
            '\nSolution: Disable the module list with parameter setting'
            '\n/MODLIST=0 (CPU object).',
      11041: 'Unauthorized characters in object name.'
            '\nThe specified object name contains unauthorized characters.'
            '\nSolution: Check the connection description.',
      11042: 'Unsupported variable type.'
            '\nCase A) Unknown identifier in object name of link node variable.'
            '\nSolution: Check the connection description.'
            '\nCase B) With parameter setting /MODLIST=0 (see CPU object of ANSL line),'
            '\ncertain variable types are not used.'
            '\nSolution: Change CPU object parameter /MODLIST.',
      11043: 'Invalid length for object name.'
            '\nThe length of the specified object name is either 0 (zero)'
            '\nor longer than 767 characters.',
      11044: 'Invalid length for BR module.'
            '\nThe length of the specified BR module is 0 (zero).',
      11045: 'Invalid variable index.'
            '\nThe specified index is invalid.'
            '\nThe addressed process variable is not an array variable or the index'
            '\nis outside the valid indexing range.'
            '\nNote: The indexing range also depends on the defined indexing type'
            '\n(parameter /ROI).',
      11046: 'Invalid structure element.'
            '\nThe specified structure element is invalid.'
            '\nThe addressed process variable is not a structure variable.',
      11150: 'Failed to install transferred BR module.'
            '\nAn error occurred while installing a BR module on the PLC.'
            '\nCause: Version conflict or configured PV memory too small.'
            '\nSolution: Rebuild the module for AR version used, configure more PV memory.'
            '\nIf this error occurs, additional information is available in the AR Logger.',       
      11151: 'Checksum check failed.'
            '\nThe checksum of the BR module is incorrect.'
            '\nSolution: Rebuild/Recompile the module.',
      11153: 'Failed to set date/time.'
            '\nThe specified values for date/time are invalid.'
            '\nSolution: Check the request data.'
            '\nIf NTP is configured on AR, setting the time is not allowed from AR A4.90 on.'
            '\nSolution: Check if the AR version is greater than or equal to A4.90'
            '\nand do not send the request.',       
      11154: 'Failed to delete BR module.'
            '\nThis error can have several causes:'
            '\n- The specified BR module cannot be found on the PLC.'
            '\n- Starting with Automation Runtime B4.33, modules that'
            '\nwere installed on the controller via project installation '
            '\n  or project update can only be deleted from the target system'
            '\nvia project installation or project update.',
      11155: 'Failed to upload BR module.\nThe specified BR module cannot be found on the PLC.',
      11156: 'Internal Automation Runtime error in connection with a download',
      11157: 'Failed to read module or library list.'
            '\nThere are no BR modules of the selected type or no libraries on the PLC.',
      11160: 'Internal Automation Runtime error when accessing a variable object',
      11161: 'Write access to variable not permitted.'
            '\nWrite access to a constant or address PV is not permitted.',
      11162: 'Failed to create BR module.'
            '\nName of BR module invalid or BR module not permitted to be created'
            '\nin the specified memory area.'
            '\nSolution: Check the module name; specify a permissible memory area.',
      11163: 'PLC restart required.'
            '\nAfter a successful download, the PLC must be restarted to complete'
            '\nthe installation.',
      11164: 'PLC not in diagnostic mode.'
            '\nThe service is only permitted to be executed in diagnostic mode.'
            '\nSolution: Set the PLC to diagnostics mode before execution.',
      11165: 'Illegal PLC memory specified.'
            '\nThe specified PLC memory cannot be found or is not permitted to be deleted.',
      11166: 'Illegal status.'
            '\nThe specified status is the current status of the task or task class.',
      11167: 'Maximum data length exceeded.'
            '\nThe maximum data length for synchronous process variables'
            '\nis limited to 4096 bytes.',
      11168: 'Synchronous data access not possible for global process variables.'
            '\nLogon with synchronous data access is not possible'
            '\nfor a global process variable.'
            '\nSolution: Use a local process variable or disable synchronous data access.',
      11169: 'Failed to create BR module in target memory.'
            '\nThe memory block for the BR module cannot be created.'
            '\nCause: Insufficient memory available or target memory too fragmented',
      11170: 'Access not permitted in PLC diagnostic mode.'
            '\nExecution of the service is not permitted in diagnostic mode.'
            '\nSolution: Set the PLC to RUN mode before execution.',
      11171: 'Internal Automation Runtime error when reading dongle list.',
      11172: 'Internal Automation Runtime error while reading license list.',
      11173: 'Internal Automation Runtime error when reading license context',
      11174: 'Failed to update license.'
            '\nThe license update could not be performed.'
            '\nCause: Invalid update file',
      11175: 'Failed to set dongle LEDs.'
            '\nThe LEDs for the specified dongle cannot be set.'
            '\nThe specified dongle is not available, cannot be reached or is defective.',
      11176: 'Not a redundant PLC system.'
            '\nThe access mode can only be executed on a redundant PLC system.',
      11177: 'The redundant CPU is not active.'
            '\nThe access mode is only permitted to be executed on the active CPU'
            '\nof a redundant PLC system.',
      11178: 'The redundant CPU is not inactive.'
            '\nThe access mode is only permitted to be executed on the inactive CPU'
            '\nof a redundant PLC system.',
      11179: 'Failed to manually switch over to redundant PLC system.'
            '\nThe redundant PLC system does not support bumpless switchover.'
            '\nSolution: Set up the redundant system for bumpless switchover.',
      11180: 'Application synchronization failed.'
            '\nAn error occurred during application synchronization in Automation Runtime.'
            '\nFor additional information, see the redundancy logbook.',
      11181: 'Failed to register tracepoint list.'
            '\nA tracepoint list is already registered for this task.',
      11182: 'Failed to activate tracepoint list.'
            '\nOne or more specified tracepoints are not valid.',
      11183: 'Failed to deregister tracepoints list.'
            '\nNo tracepoint list is registered for this task.',
      11184: 'Failed to read tracepoint data.'
            '\nNo current tracepoint data is available for this task.',
      11185: 'Error reading extended CPU information.'
            '\nAn error occurred while reading the extended CPU information'
            '\n(table of contents) in Automation Runtime.',
      11186: 'The pointer of the dynamic variable is NULL.'
            '\nThe dynamic variable cannot be accessed because the pointer'
            '\nis not defined (NULL).',
      11187: 'Uninstalling/Deleting module not permitted.'
            '\nThe module is not permitted to be uninstalled/deleted'
            '\n(e.g. system logbook) or must be uninstalled/deleted in the context'
            '\nof a transfer module.',
      11188: 'Module used by another module and cannot be deleted.'
            '\nAttempted to delete a module that still has dependencies on other modules'
            '\n(e.g. deleting a library) or which is used in a task and therefore'
            '\ncannot be deleted.',
      11189: 'Connection marked as redundancy-relevant.'
            '\nThe connection is marked as redundancy-relevant and therefore'
            '\nresults in a redundancy switchover when the connection is lost.',
      11190: 'Connection not marked as redundancy-relevant.'
            '\nThe connection is not marked as redundancy-relevant and therefore'
            '\ndoes not result in a redundancy switchover when the connection is lost.',
      11191: 'Specified identification number invalid.'
            '\nThere is no valid entry for the identification number specified'
            '\nin parameter ID.'
            '\nThis error can only occur when reading the entries of a BR log data module'
            '\nin XML format (access type POBJ_ACC_LN_XML_LOGM_DATA).',
      11192: 'Redundancy-relevant connection aborted.'
            '\n A connection marked as redundancy-relevant has been aborted and can result'
            '\nin a redundancy switchover on the AR side.',
      11193: 'Specified object not supported.'
            '\nThe object specified in the transfer service is not supported'
            '\nby the ANSL online server.'
            '\nPossible causes: Incorrect specification in the request data'
            '\nor the AR version being used is obsolete.',
      11194: 'Specified object not available.'
            '\nThe object specified in the transfer service or directory'
            '\nin not available in AR.',
      11195: 'Authentication failed when logging on to AR.'
            '\nThe specified username or password is incorrect (PVI parameters /UN and /PW).',
      11196: 'Execution of service denied.'
            '\nThe logged in user is not authorized to execute this service.',
      11221: 'XML parser initialization error.'
            '\nThe XML parser in AR could not be initialized.',
      11222: 'Invalid XML data.'
            '\nThe specified or read XML data is invalid.',
      11230: 'Invalid XML element.'
            '\nThe specified or read XML data is invalid contains at least'
            '\none invalid XML element.',
      11231: 'Invalid XML attribute.'
            '\nThe specified or read XML data is invalid contains at least'
            '\none invalid XML attribute.',
      11232: 'Missing required XML attribute.'
            '\nAn attribute required for the service is not specified'
            '\nin the XML request data.',
      12000: 'Undefinable error'
            '\nAn attributable error was generated in the PVI Manager.'
            '\nThis is an internal PVI error.',
      12001: 'The object handle list is full.'
            '\nThe number of link objects or process objects (service objects)'
            '\nexceeds 2147483647.',
      12002: 'Object name already exists'
            '\nThe symbolic process object name is already in use.'
            '\nThe process object cannot be set up under this name.'
            '\nThis error is returned when setting up a static process object'
            '\nin the PviCreate or PviCreateResponse function.'
            '\nWhen you try to set up a temporary process object, '
            '\na link object is set up to the existing process object with the specified name.',
      12003: 'Object name not found'
            '\nCase A): There is no symbolic process object name in the process object path.'
            '\nThis error occurs with PviCreate, PviLink and PviDelete.'
            '\nCase B): The symbolic process object name cannot be found.'
            '\nThis can only be the case with PviLink or PviDelete.',
      12004: 'Undefined object handle'
            '\nThe connection object handle (LinkID) specified in the user function'
            '\n(PviRead, PviWrite, PviChgLink and Unlink) is not valid.'
            '\nThere is no corresponding connection object.',
      12005: 'Illegal object type'
            '\nThe object type specified in the PviCreate, PviLink or PviDelete function'
            '\nin the symbolic object path'
            '\n(in string format) is not known to PVI.'
            '\nExample @/Pvi/LNINA2 OT=XYZ/Station'
            '\nThe object type [ number (in binary format) ] specified as the argument'
            '\nin the PviCreate function is not known to PVI.'
            '\nCurrently valid object types: 1..7',
      12006: 'Illegal length of object name'
            '\nThe length of the symbolic process object name is not permitted.'
            '\nAn empty object name was specified in the process object path'
            '\nor the length of the process object path is greater than MAXLEN_POBJ_NAME'
            '\ncharacters.'
            '\nMAXLEN_POBJ_NAME is currently limited to 256 characters.',
      12007: 'Syntax error in object name'
            '\nA syntax error was detected in the process object name or process object path.'
            '\nThe process object path represents the process object hierarchy.'
            '\nTo uniquely separate the process object names within a process object path,'
            '\nthey are subject to fixed syntax rules.'
            '\nA typical error is that the process object name is not placed inside'
            '\nquotation marks when it includes blanks or special characters.'
            '\nExample:'
            '\n   Incorrect: @/Pvi/Lnina2/COM2/ST1/CP260 Main extruder/TempHigh'
            '\n   Correct: @/Pvi/Lnina2/COM2/ST1/CP260 Main extruder/TempHigh'
            '\nSee PVI documentation, chapter Characters in object names and object'
            '\ndescriptions and chapter Process object names and connection description.',
      12008: 'Syntax error in connection description'
            '\nThis error only occurs if addressing via Unique object names is used'
            '\ninstead of Path specification.'
            '\nThe error occurs with parameter CD or with write access to the'
            '\nconnection description.'
            '\nThe connection description does adhere to the syntax rules'
            '\nfor process object names.'
            '\nAs described for error 12007, the rules are only applied to the'
            '\nconnection description.',
      12009: 'Illegal object hierarchy'
            '\nThe specified process object type (for example: Line, Device, Task, Pvar) '
            '\nis not compatible with that of the higher-level process object.'
            '\nThis is the case if attempting to set up a device process object'
            '\nunder a task process object, for example.',
      12011: 'Requested memory cannot be reserved'
            '\nThe memory request returns an error.'
            '\nNot enough memory available, no reservation possible.',
      12012: 'Illegal data length'
            '\nCase A) The number of specified request data bytes'
            '\n(user function PviRead, PviWrite) is greater'
            '\nor less than allowed for this request (depending on the access mode).'
            '\nCase B) The maximum number of 2147483647 request data bytes was exceeded.',
      12013: 'Process object has no valid variable data'
            '\nThis error mainly occurs with internal variables that are read'
            '\nbefore they are written to for the first time.',
      12014: 'Limit exceeded.'
            '\nLimit values specified in the process object or in the'
            '\nconnection object were exceeded.'
            '\nThe limit values are defined with parameter FS.'
            '\nThis error can only occur in response to a write request'
            '\n(user function PviWrite).',
      12015: 'Specified object name not unique.'
            '\nAt least 2 process objects exist for a process object name specified'
            '\nin the object path (when using pathnames)'
            '\nor specified in parameter CD (when using unique object names).'
            '\nThe object assignment is therefore not unique.'
            '\nSolution: In the object path, the process object can be determined'
            '\nby specifying the object type (example:@Pvi/.../Test OT=Task/Var1).'
            '\nIf unique object names are used, the object type cannot be specified'
            '\nin parameter CD.'
            '\nIn this case, the process object names must be changed accordingly.',
      12020:'Syntax error in a description string.'
            '\nThere is at least one syntax error in the specified connection object'
            '\nor process object description (user function PviCreate or PviLink)'
            '\nor in the string passed with write access (user function PviWrite)'
            '\nto an object property'
            '\n(access type TYPE, CONNECT, etc.).',
      12021: 'Unknown keyword in PVI description string'
            '\nThe specified connection object or process object description'
            '\n(user function PviCreate or PviLink) contains at least one unknown PVI keyword.'
            '\nExample:'
            '\nIncorrect: RF=1500 VT=u8 QW=2'
            '\nCorrect: RF=1500 VT=u8.',
      12022: 'Keyword already exists in description.'
            '\nAt least one PVI keyword is found more than once in the specified'
            '\nconnection object'
            '\nor process object description (user function PviCreate or PviLink).'
            '\nExample:'
            '\nIncorrect: RF=200 VT=u8 RF=200'
            '\nCorrect: VT=u8 RF=200',
      12023: 'Impermissible keyword in description'
            '\nA PVI keyword is not permitted for this process object type'
            '\nin the specified connection object'
            '\nor process object description (user function PviCreate or PviLink).'
            '\nExample: The specification of a variable type (VT=u8) in connection'
            '\nwith a task object is not permitted.',
      12024: 'Maximum nesting depth or number of elements in structure variable exceeded'
            '\nThe maximum nesting depth or the maximum number of elements'
            '\nin a structure variable has been exceeded.'
            '\nCurrently, the maximum nesting depth in PVI is limited to 64.'
            '\nThe maximum number of structure elements is limited to 65535.'
            '\nKeep the following in mind when calculating the number of elements'
            '\nin a structure:'
            '\nIf a structure contains further structures, the structure itself'
            '\nand its structure elements must also be counted.',
      12025: 'Illegal nesting in structure variable'
            '\nThe structure specified in the description string'
            '\n(connection object or process object description or access type TYPE)'
            '\nas data format was specified with incorrect nesting.',
      12026: 'Impermissible scaling or limit value specification'
            '\nAn invalid scaling or limit value specification is contained'
            '\nin the parameter specification FS'
            '\nof the connection object or process object description'
            '\n(user function PviCreate or PviLink)'
            '\nor in the string passed when accessing the object property FUNCTION'
            '\n(user function PviWrite).'
            '\nImpermissible entries include: '
            '\n1) The maximum number of function value pairs has been exceeded.'
            '\n   Currently, a maximum of 32766 value pairs can be specified.'
            '\n2) An odd number of function values was specified.'
            '\n3) Syntax error (e.g. function or limit value specification'
            '\ncontains invalid separator).',
      12027: 'Impermissible scaling or limit value'
            '\nAt least one impermissible scaling or limit value is contained'
            '\nin the parameter specification FS'
            '\nof the connection object or process object description'
            '\n(user function PviCreate or PviLink)'
            '\nor in the string passed when accessing the object property FUNCTION'
            '\n(user function PviWrite).'
            '\nThe specified function is not strictly monotonically increasing or'
            '\nstrictly monotonically decreasing.',
      12028: 'Impermissible hysteresis value specification'
            '\nAn impermissible hysteresis value is contained in the parameter specification HY'
            '\nof the connection object or process object description'
            '\n(user function PviCreate or PviLink)'
            '\nor in the string passed when accessing the object property HYSTERESIS'
            '\n(user function PviWrite).',
      12030: 'Unsupported property'
            '\nAn attempt was made to read or write a property not supported'
            '\nor unknown by the addressed object.'
            '\nThis is an internal PVI error.',
      12031: 'Unsupported status'
            '\nAn attempt was made to read or write a status that is not supported'
            '\nby the addressed object.'
            '\nThis is an internal PVI error.',
      12032: 'No data format defined'
            '\nA hysteresis or function was defined in the connection object description'
            '\nwithout specifying a data format.',
      12033: 'Illegal data format'
            '\nCase A) The existing data format (connection object or process object)'
            '\ncannot be used for variable addressing.'
            '\nCase B) An illegal data format is defined in the data format specification'
            '\nof the connection object'
            '\nor process object description (user function PviCreate or PviLink)'
            '\nor in the string passed with a write access (user function PviWrite)'
            '\nto the object property TYPE.',
      12034: 'Write-protected object.'
            '\nAn attempt was made to write to a process variable'
            '\nwith write protection enabled.'
            '\nWrite protection can be set by the user (e.g. parameter AT=r)'
            '\nor by the line.',
      12035: 'Read-protected object.'
            '\nAn attempt was made to read a process variable with read protection enabled.'
            '\nRead protection can be defined by the user (e.g. parameter AT=w)'
            '\nor by the line.',
      12036: 'Data type conflict (cast with incompatible data types).'
            '\nData type conversion (cast) between connection and process object'
            '\ncannot be performed with the existing data formats.'
            '\nFor example: cast between integer and structure.',
      12037: 'Data length conflict.'
            '\nCase A) Error in the description string for the data format.'
            '\n  A data length specified by the variable type (parameter VT)'
            '\n  is not equal to the specified data length.'
            '\n  Example: Incorrect: VT=u16 VL=3 Correct: VT=u16 VL=2'
            '\n  or simply VT=u16.'
            '\nCase B) When writing to a variable object (PviWrite), a buffer length was'
            '\n  specified that does not match the length of the variable data.'
            '\n  A smaller buffer length can only be specified for variable types'
            '\n  string and wstring.',
      12038: 'Illegal data format for hysteresis or function.'
            '\nThe hysteresis or scaling function or limit monitoring cannot work'
            '\nwith the existing data format of the variable.'
            '\nExample: Hysteresis not possible with structure variables',
      12039: 'Data format defined by line.'
            '\nAn attempt was made to overwrite (access mode: TYPE) a data'
            '\nformat defined by the line (e.g. for NET2000 and INA2000 lines).',
      12040: 'Connection aborted.'
            '\nA connection to a process object via a connection object was aborted.'
            '\nThe following causes are possible:'
            '\n1) PVI Manager was closed.'
            '\n2) The process object was deleted (user function PviDelete).'
            '\n3) The trial time has expired.',
      12041: 'Error registering application.'
            '\nReserved error - not used',
      12042: 'Unregistered application.'
            '\nThis error occurs when a request is received from a client (application)'
            '\nthat is not registered on the server (manager).'
            '\nThis is an internal PVI error and is only visible in the data logger.',
      12043: 'Request aborted.'
            '\nA request initiated by the application was aborted prematurely.'
            '\nThis can have the following causes:'
            '\n1) The request was aborted by a command in the application itself'
            '\n(access type CANCEL).'
            '\n2) The corresponding process object has been deleted (PviDelete).',
      12044: 'Maximum number of application instances (clients) exceeded.'
            '\nThe maximum number of application instances (clients)'
            '\nthat can be registered on the PVI Manager has been exceeded.'
            '\nThe maximum number is currently limited to 65534.',
      12045: 'Invalid instance handle (client).'
            '\nAn invalid handle for the application instance was passed'
            '\nto the user function (PviX.....).',
      12050: 'PVI Manager not started.'
            '\nThe PVI Manager has not been started or registered.'
            '\nThis error can only occur in connection with local client/server'
            '\n(application/PVI Manager) communication.',
      12051: 'Error communicating with PVI Manager.'
            '\nReserved error - not used',
      12052: 'Incorrect version of communication DLL.'
            '\nThe version of the communication library PviCom.dll used'
            '\nby the client (application)'
            '\nis not compatible with the version used by the server (PVI Manager).',
      12053: 'Illegal request data.'
            '\nImpermissible request data was read from the server.'
            '\nImpermissible request data can only occur during TCP/IP communication'
            '\nbetween client (application) and server (PVI Manager)'
            '\nif an external (non-PVI) application tries to establish a connection'
            '\non the same port number.',
      12054: 'Illegal response data.'
            '\nImpermissible response data was read from the client.'
            '\nError behavior analogous to error 12053.',
      12055: 'No response data found.'
            '\nWhen calling the function PviGetResponseInfo or one of the reply'
            '\nfunctions Pvi...Response, no corresponding response data was found.'
            '\nThe following causes are possible:'
            '\n1) The message parameter (wParam) specified in the function call is incorrect.'
            '\n2) The response function Pvi...Response has already been called for the'
            '\nmessage parameter.'
            '\n3) The response data (response or event data) has already been deleted'
            '\nby calling function PviUnlink or PviUnlinkAll.',
      12056: 'Impermissible use of C functions.'
            '\nThe called response function (Pvi...Response) does not match'
            '\nthe response data mode.'
            '\nThis mode (Create, Link, Read, Write, etc.) is determined'
            '\nby the request function used'
            '\n(PviCreateRequest, PviLinkRequest, PviReadRequest, PviWriteRequest, etc.).'
            '\nThus, response data for function PviLinkRequest can only be read'
            '\nwith PviLinkResponse,'
            '\nand response data for function PviWriteRequest can only be read'
            '\nwith PviWriteResponse.'
            '\nEvent data can only be read with the response function PviReadResponse.',
      12057: 'Illegal window handle.'
            '\nThe message pointer/handle specified in function PviLinkRequest is'
            '\nnot permitted (== NULL).',
      12058: 'Unsupported access mode.'
            '\nThe access mode passed with user function PviRead or PviWrite'
            '\nis not supported by the type of the addressed process object'
            '\nor by the line used.',
      12059: 'Communication timeout (application / PVI Manager).'
            '\nThe time defined by the user with function PviInitialize'
            '\n(function argument Timeout)'
            '\nfor client/server (application / PVI Manager) communication has expired.'
            '\nThe application could not communicate with the PVI Manager during this time.',
      12060: 'Process timeout (request/response).'
            '\nThe time defined by the user with function PviInitialize (parameter PT)'
            '\nfor request processing (request/response) has expired.'
            '\nThe request was aborted.'
            '\nThe timeout for request processing defines the maximum time'
            '\nthat is permitted to elapse'
            '\nbefore the response data of a request has been sent to the'
            '\napplication by the PVI Manager.',
      12062: 'PVICOM not initialized / already initialized.'
            '\n1) After starting the application or after calling function PviDeinitialize, '
            '\n   a user function other than PviInitialize was called.'
            '\n2) User function PviInitialize (without error response) was called'
            '\na second time'
            '\n   without first calling function PviDeinitialize.',
      12063: 'Illegal function parameter.'
            '\nA user function was provided with an impermissible function parameter.'
            '\nExample: If a value other than zero was specified for the last'
            '\nparameter (pRes) of function PviInitialize.',
      12064: 'No access privilegs to start windows service "B&R PVI Manager".'
            '\n"B&R PVI Manager" is installed as a windows service on that system'
            '\nbut it is currently not running.'
            '\nThe current user privilegs do not allow to start the service automatically.'
            '\nYou have to start this service manually.',
      12070: 'Error loading line DLL.\nThe line object could not load the line DLL.'
            '\nMost common cause: The line DLL defined with the connection description'
            '\nor one of its components could not be found.'
            '\nThe error reported by Windows can be read from the log file'
            '\nof the PVI Manager (see PVI data logger).',
      12071: 'Error identifying line DLL.'
            '\nThe DLL defined with the connection description of the line object'
            '\ncould be loaded.'
            '\nHowever, the DLL was not recognized by the PVI Manager as a valid line DLL.'
            '\nThere may be a version conflict. ',
      12072: 'Undefinable line error message.'
            '\nAn unattributable error was reported by the line to the PVI Manager.'
            '\nUnattributable errors are errors with an error code less than or equal to 0'
            '\nor greater than 65535.'
            '\nThe error code that was actually given can only be determined with the'
            '\nPVI data logger with Mode=3.',
      12073: 'Impermissible line name.'
            '\nThe name of the line DLL defined with the connection description of the'
            '\nline object is impermissible.'
            '\nThe error reported by Windows can be read from the PVI Manager'
            '\nlog file (see PVI data logger).',
      12074: 'Component for generating BR modules not installed',                
      12075: 'Error loading function DLL'
            '\nThe variable object could not load the function DLL.'
            '\nMost common cause: No corresponding function DLL could be found'
            '\nfor the defined data function.'
            '\nThe error reported by Windows can be read from the log file'
            '\nof the PVI Manager (see PVI data logger).',
      12076: 'Error identifying function DLL.'
            '\nA DLL could be loaded for the data function defined in the variable object.'
            '\nHowever, the DLL was not recognized by the PVI Manager as a function DLL.',
      12077: 'Impermissible function name'
            '\nThe function name defined with the data function is not permissible.'
            '\nThe error reported by Windows can be read from the PVI Manager log file'
            '\n(see PVI data logger).',
      12080: 'PVI system error (illegal value format).'
            '\nAn illegal value format was specified.'
            '\nThis is an internal error of the PVI Manager.',
      12081: 'PVI system error (internal PVI data damaged).'
            '\nInternal PVI Manager data is corrupted.'
            '\nThis is an internal error of the PVI Manager.',
      12082: 'Line system error (unauthorized access to line interface function).'
            '\nUnauthorized access to line interface function.'
            '\nThis is an internal error of the PVI line interface.',
      12083: 'Line system error (unauthorized process suspension).'
            '\nUnauthorized process suspension.'
            '\nThis is an internal error of the PVI line interface.',
      12084: 'Line system error (illegal process object handle).'
            '\nIllegal process object handle.'
            '\nThis is an internal error of the PVI line interface.',
      12085: 'PVI/line system error (undefined service status).'
            '\nUndefined service status.'
            '\nThis is an internal error of the PVI line interface or the PVI Manager.',
      12086: 'Incorrect line DLL version.'
            '\nThe line DLL version used is not compatible with the PVI Manager.',
      12090: 'General socket error (TCP/IP error).'
            '\nGeneral socket error (TCP/IP error).'
            '\nThe error reported by Windows can be read from the log file of the'
            '\ncommunication DLL PviCom client'
            '\nor server instance (see PVI data logger).',
      12091: 'Incorrect IP address or hostname not available (TCP/IP error).'
            '\nIncorrect IP address or hostname not available (TCP/IP error).'
            '\nThe error reported by Windows can be read from the log file of the'
            '\ncommunication DLL PviCom client'
            '\nor server instance (see PVI data logger).',
      12092: 'Error in network subsystem (TCP/IP error).'
            '\nError in the network subsystem (TCP/IP error).'
            '\nThe error reported by Windows can be read from the log file of the'
            '\ncommunication DLL PviCom client'
            '\nor server instance (see PVI data logger).',
      12093: 'Memory error or limit reached (TCP/IP error).'
            '\nMemory error or limit reached (TCP/IP error).'
            '\nThe error reported by Windows can be read from the log file of the'
            '\ncommunication DLL PviCom client'
            '\nor server instance (see PVI data logger).',
      12094: 'Communication not possible (TCP/IP error).'
            '\nCommunication not possible (TCP/IP error).'
            '\nThe error reported by Windows can be read from the log file of the'
            '\ncommunication DLL PviCom client'
            '\nor server instance (see PVI data logger).',
      12095: 'Communication malfunction (TCP/IP error).'
            '\nCommunication malfunction (TCP/IP error).'
            '\nThe error reported by Windows can be read from the log file of the'
            '\ncommunication DLL PviCom client'
            '\nor server instance (see PVI data logger).',
      12096: 'Host not found or malfunctioning (TCP/IP error).'
            '\nHost not found or malfunctioning (TCP/IP error).'
            '\nThe error reported by Windows can be read from the log file of the'
            '\ncommunication DLL PviCom client'
            '\nor server instance (see PVI data logger).',
      12100: 'Windows system error when setting up system resource.'
            '\nAn attempt to set up a system resource was denied by Windows with an error.'
            '\nThe error reported by Windows can be read from the log file of the PVI Manager'
            '\nor the communication DLL PviCom client or server instance (see PVI data logger).',
      12101: 'Windows system error: Wait function.'
            '\nError executing the wait function.'
            '\nThe error reported by Windows can be read from the log file of the PVI Manager'
            '\nor the communication DLL PviCom client or server instance (see PVI data logger).',
      12102: 'Windows system error: Set up / open events.'
            '\nAn attempt to set up or open a system event was denied by Windows with an error.'
            '\nThe error reported by Windows can be read from the log file of the PVI Manager'
            '\nor the communication DLL PviCom client or server instance (see PVI data logger).',
      12103: 'Windows system error: Set up / open mapped file (communication buffer).'
            '\nAn attempt to set up or open a mapped file (communication buffer) was denied'
            '\nby Windows with an error.'
            '\nThe error reported by Windows can be read from the log file of the PVI Manager'
            '\nor the communication DLL PviCom client or server instance (see PVI data logger).',
      12104: 'Windows system error: Set up / start thread.'
            '\nAn attempt to create or start a thread was denied by Windows with an error.'
            '\nThe error reported by Windows can be read from the log file of the PVI Manager'
            '\nor the communication DLL PviCom client or server instance (see PVI data logger).',
      12105: 'Windows system error: Install / uninstall service'
            '\nAn attempt to install or uninstall the PVI Manager as a service was denied'
            '\nby Windows with an error.'
            '\nThe error reported by Windows can be read from the log file of the'
            '\nPVI Manager (see PVI data logger).',
      12106: 'Windows system error: Access to registry'
            '\nAccess to the registry was denied by Windows with an error.'
            '\nThe error reported by Windows can be read from the log file of the'
            '\nPVI Manager (see PVI data logger).',
      12107: 'Windows system error: Access to firewall'
            '\nAccess to the firewall was denied by Windows with an error.'
            '\nThe error reported by Windows can be read from the log file of the'
            '\nPVI Manager (see PVI data logger).',
      12120: 'Path/File not found.'
            '\nA drive or directory specified in the path name cannot be found.'
            '\nThe specified file cannot be found.',
      12121: 'Invalid path or file name.'
            '\nThe specified path or file name is invalid'
            '\n(e.g. impermissible characters were used in the name = syntax error).',
      12122: 'Access denied.'
            '\nAccess to the drive, directory or file has been denied by the operating system.'
            '\nPossible cause: File already opened by another program ',
      12123: 'Device is write-protected'
            '\nThe specified device is write-protected.',
      12124: 'Device not ready.'
            '\nThe specified device is not ready.',
      12125: 'Error setting up / opening file.'
            '\nThe operating system reports an error when setting up or opening a file.',        
      12126: 'Write error'
            '\nThe operating system reports an error when writing data to a file.',
      12127: 'Read error'
            '\nThe operating system reports an error when reading data from a file.',
      12128: 'Error deleting file'
            '\nThe operating system reports an error when deleting a file.',
      12129: 'Error executing file'
            '\nThe operating system reports an error when executing a file.',        
      12130: 'File already exists'
            '\nAn attempt was made to set up a file that already exists.',
      12500: 'Internal error of the NET2000 library (Net2000.dll).',
      12510: 'Timeout during communication with the slave.'
            '\nTimeout during communication with the slave.'
            '\nPossible cause: Net2000 timeout parameter too low, connection interrupted',
      12520: 'Master receive buffer could not be allocated (insufficient memory).',
      12521: 'The master receive buffer is too small to receive slave data.',
      12522: 'Communication status error (data blocks lost)',
      12540: 'Slave not ready',
      12541: 'Master send buffer could not be allocated (too little memory)',
      12542: 'Master send buffer too small to receive slave data',
      12543: 'Illegal data received from slave, incorrect sequence number.'
            '\nPossible cause: Master restarted without resetting slave',
      12544: 'Illegal data received from slave, incorrect service code.'
            '\nPossible cause: Master restarted without resetting slave',
      12545: 'Illegal data received from slave, incorrect data length.'
            '\nPossible causes: The master was restarted without resetting the slave.'
            '\nThe byte alignment of an addressed PLC structure variable does not match'
            '\nthe one expected by the master.'
            '\nSolution: Change all byte structure elements to type WORD / INT16'
            '\nor insert fill bytes.',
      12560: 'Data buffer too small.'
            '\nPossible cause: Problem with spoio_in_len when calling dsf_action',
      12561: 'Illegal call code.'
            '\nPossible cause: Software version',
      12580: 'Memory could not be allocated (Create)',
      12581: 'Memory could not be allocated (init)',
      12600: 'Slave: Fatal error',
      12601: 'Slave: No response buffer (layer 7) of corresponding size available',
      12602: 'Slave: Illegal object index.'
            '\nPossible cause: Version problem, changes made on slave',
      12603: 'Slave: Illegal call code (service not supported)',
      12604: 'Slave: Illegal channel number (check software versions)',
      12605: 'Slave: Incorrect syntax for event-driven object (event list)',
      12606: 'Slave: Event manager not installed',
      12607: 'Slave: Event list configured too small',
      12608: 'Slave: Object not a structure',
      12609: 'Slave: Read error from object structure',
      12610: 'Slave: Master other than event master attempt. to register event-controlled PVs',
      12611: 'Slave: Object index error / index out of range',
      12612: 'Slave: No request buffer (layer 7) of corresponding size available',
      12613: 'Slave: No confirmation buffer (layer 4 or 7) of corresponding size available',
      12614: 'Slave: No indication buffer (layer 4 or 7) of corresponding size available',
      12670: 'Slave: Invalid object type',
      12671: 'Slave: Unknown object.\nSlave: Master other than event master attempting'
              '\nto register event-controlled PVs',
      12672: 'Slave: Object index table is full',
      12700: 'DSF not yet initialized (by calling dsf_action before dsf_open)',
      12701: 'Memory error in init part (memory request leads to error)',
      12702: 'Invalid action code of DSF state machine (possible version problem)',
      12703: 'Error setting up / closing communication thread',
      12704: 'Error setting up / closing communication event',
      12755: 'Error in NET2000 master library or PLC.\nDetermine NET2000 error code (1 byte)',
      12756: 'Error initializing NET2000 DLL',
      12758: 'Illegal object hierarchy.'
            '\nThe process objects of the NET2000 line have an illegal object hierarchy.'
            '\nExample: A variable object has been set up under a device object'
            '\n(without a station object).'
            '\nHowever, the Net2000 line requires both a device object and a station object.',
      12759: 'NET2000 protocol error.'
            '\nA NET2000 protocol error has occurred.'
            '\nThis is an internal error caused by a malfunction of the NET2000 state machine.',
      12760: 'Fatal error.'
            '\nInternal error of the NET2000 line',
      12761: 'Maximum NET2000 protocol length too small'
            '\nThe maximum transferable variable data length has been exceeded.'
            '\nThe NET2000 protocol can only transfer variable data up to a maximum length.'
            '\nThis maximum length is determined from the l7length set in the PLC'
            '\n(see NET2000 structure) minus a protocol header of 20 bytes.'
            '\nA maximum of 32747 bytes is permitted to be set for l7length.',
      12762: 'Illegal object name.'
            '\nThe name of the line object is illegal.'
            '\nThe length of the variable name and task name (if any) is greater'
            '\nthan 1024 bytes.'
            '\nThe name of the line object is determined by the connection name'
            '\n(PVI parameter CD).',
      12763: 'PLC does not support events or event module not installed.'
            '\nThe connected PLC does not support any events or the event module'
            '\nis not installed on the PLC.',
      12900: 'Data buffer not set up',
      12901: 'Invalid data format',
      12902: 'Device not found',        
      13000: 'Undefined INAFRM.DLL error',
      13001: 'Active request still active (in import request)',
      13002: 'Active request still active (in send request)',
      13003: 'Error closing interface',
      13004: 'Error reading from interface',
      13005: 'Error writing via interface',
      13006: 'Driver not found, cannot be loaded',
      13007: 'Error in device name - IF parameter (e.g. incorrect COM number)',
      13008: 'Illegal data received',
      13009: 'Illegal device handle',
      13010: 'Illegal destination address (e.g. parameter DA: station number, station name)',
      13011: 'Invalid parameter in connection description (initialization string)',
      13012: 'Unauthorized parameter change',
      13013: 'Illegal data length for import request',
      13014: 'Illegal data length for send request',
      13015: 'Illegal source address (e.g. parameter SA: station number, station name)',
      13016: 'Illegal station handle',
      13017: 'No ID list specified',
      13018: 'Insufficient RAM',
      13019: 'Device closed (connection aborted)',
      13020: 'No confirmation data found for read request',
      13021: 'No confirmation data found for send request',
      13022: 'Error reading interface parameters',
      13024: 'Unknown device (e.g. parameter IF: device name)',
      13025: 'Unsupported function',
      13026: 'Error writing interface parameters',
      13027: 'Windows resource error (events, etc.)',
      13028: 'Station or device already in use',
      13029: 'Failed to set up transfer thread',        
      13030: 'Unknown target address (e.g. parameter DA: station number, station name)',
      13033: 'Error in network configuration (parameter DA)'
            '\nThe specified target station number is not unique within the IP network.'
            '\nThere are at least 2 stations with the same station number.'
            '\nSolution: Set a unique station number with the node switches'
            '\n(or in the system configuration) of the PLC'
            '\nor use parameter DAIP.',
      13034: 'Error in network configuration (parameter SA)'
            '\nUnknown target address (e.g. parameter DA: station number, station name).'
            '\nThere are at least 2 stations with the same station number.'
            '\nSolution: Use a unique station number for the source station.',
      13035: 'Read timeout error',
      13036: 'Write timeout error',
      13037: 'INA frame library INAFRMS.DLL not found or cannot be loaded',
      13040: 'Error downloading PROFIBUS firmware',
      13041: 'Error downloading PROFIBUS network configuration module',
      13042: 'Error setting up PROFIBUS read/write threads',
      13045: 'Error during initialization TAPI was possibly not installed correctly.'
              '\n(See modem installation)',
      13046: 'No modems installed',
      13047: 'Invalid modem name.'
            '\nThe specified modem name could be found, but the corresponding device'
            '\ndoes not have the required properties,'
            '\ni.e. it is not a modem.',
      13048: 'Modem not found.'
            '\nA modem with the specified name could not be found.'
            '\nCheck whether the name is correct and install the corresponding modem'
            '\nif necessary.',
      13049: 'TAPI version not supported.'
            '\nThe installed TAPI version is not supported.'
            '\nPlease use Tapi Version 2.0 or higher.',
      13050: 'Error calling TAPI function (operating system error message)',
      13051: 'TAPI device already in use by another Windows program',
      13052: 'No free channels',
      13053: 'Incorrect phone number format.'
            '\nThe format of the telephone number is not correct.'
            '\nThe complete telephone number in international format (canonical format)'
            '\nmust always be used. (e.g. +43(7748)6586 999)',
      13054: 'Error establishing connection',
      13055: 'No response was received from the modem.'
            '\nThere may be a wiring problem. Example: Modem not connected to computer',
      13056: 'Modem failed to dial.'
            '\nThe modem may not be connected to the telephone line,'
            '\nthere is no dial tone, the line is busy, etc.',
      13057: 'Error occurs when modem switched off',
      13058: 'Incorrect TAPI version installed (e.g. 1.4).'
            '\nSolution: Install version 2.0 or 2.1.',
      13059: 'An existing connection was interrupted.'
            '\nAn existing connection was interrupted.'
            '\nPossible causes: Modem switched off, telephone cable disconnected, etc.',
      13060: 'Error during initialization.'
            '\nSystem resources required for operation could not be requested.',
      13061: 'Missing parameters: /MO and /TN must be specified',
      13070: 'Access denied (5, ERROR_ACCESS_DENIED).'
            '\nAccess to a file or device has been denied by the system.'
            '\nPossible cause: The specified file (parameter /SP (save path)'
            '\nor /MP (module path) in the port description of the CPU object)'
            '\nor the specified device (parameter /IF in the port description'
            '\nof the device object) is being used by another program.',
      13071: 'Device does not recognize command (22, ERROR_BAD_COMMAND)',
      13072: 'Specified device invalid (1200, ERROR_BAD_DEVICE)',
      13073: 'Specified device not found (20, ERROR_BAD_UNIT)',
      13074: 'Insufficient memory on drive (112, ERROR_DISK_FULL)',
      13075: 'Module not found (126, ERROR_MOD_NOT_FOUND)',
      13076: 'Specified device (parameter /IF) not found (2, ERROR_FILE_NOT_FOUND)',
      13077: 'Device in the system does not work (31, ERROR_GEN_FAILURE)',
      13078: 'Invalid flags (1004, ERROR_INVALID_FLAGS)',
      13079: 'Incorrect syntax for file name, directory name or drive name'
	  		'\n(123, ERROR_INVALID_NAME)',
      13080: 'Invalid function (1, ERROR_INVALID_FUNCTION)',
      13081: 'Access code invalid (12, ERROR_INVALID_ACCESS)',
      13082: 'Invalid handle (6, ERROR_INVALID_HANDLE)',
      13083: 'Insufficient memory to execute command (8, ERROR_NOT_ENOUGH_MEMORY)',
      13084: 'Device not ready (21, ERROR_NOT_READY)',
      13085: 'System cannot open device (110, ERROR_OPEN_FAILED)',
      13086: 'Path not found (3, ERROR_PATH_NOT_FOUND)',
      13087: 'System cannot read from specified device (30, ERROR_READ_FAULT)',
      13088: 'Recursion too low - stack overflow (1001, ERROR_STACK_OVERFLOW)',
      13089: 'System cannot write to specified device (29, ERROR_WRITE_FAULT)',
      13090: 'Incorrect Winsock version',
      13091: 'Error during initialization (Winsock)',
      13092: 'Error setting up socket',
      13093: 'General TCP/IP error',
      13094: 'Port in use',
      13095: 'Error binding socket',
      13096: 'Failed to set up thread',
      13097: 'Station number not found',
      13098: 'Winsock not installed.'
            '\nSolution: Win95: Execute installer file ...\Pvi\SysSetup\TcpIp\Sock2295.exe.',        
      13200: 'Internal error in CAN driver',
      13201: 'Invalid parameter.'
            '\nAn invalid parameter was passed to DeviceIoControl,'
            '\ne.g. NULL pointer for <OutBuf> for IOTCL_INACAN_READ.',
      13202: 'Incorrect length.'
            '\nAn incorrect data length was passed to DeviceIoControl,'
            '\ne.g. the size of <InBuf> for IOTCL_INACAN_SETPAR does not match'
            '\nthe size of structure INACAN_CONFIG.',
      13203: 'I/O still busy.'
            '\nWhen IOTCL_INACAN_READ or IOTCL_INACAN_WRITE was called,'
            '\nan asynchronous call of the same function was still active.'
            '\nA new call is only possible after the active call has ended'
            '\nor been aborted (with IOTCL_INACAN_CANCEL).',
      13204: 'Function not supported.'
            '\nAn unknown function code was specified when calling DeviceIoControl.',
      13205: 'Invalid memory access.'
            '\nThe CAN controller could not be accessed, e.g. because an incorrect'
            '\nsegment address was specified for IOCTL_INACAN_SETPAR.',
      13206: 'Interrupt cannot be activated.'
            '\nWindows system error: The interrupt with the IRQ number specified'
            '\nin IOTCL_INACAN_SETPAR could not be activated.'
            '\nThe IRQ number may be invalid or already used by another device.',
      13207: 'No confirmation',
      13208: 'Receive buffer overflow.'
            '\nThe receive FIFO filled up, e.g. because the application'
            '\ndoes not call IOTCL_INACAN_READ fast enough to read the pending CAN messages.',
      13209: 'Error while reading (messages lost).'
            '\nError while reading the receive object from the CAN controller:'
            '\nCAN messages were lost.'
            '\nThe PC may be too slow to process the messages occurring on the CAN bus.',
      13210: 'Write error.'
            '\nInternal driver error: Error while writing the transmit object'
            '\nfrom the CAN controller,'
            '\ne.g. invalid object number, send request is still active'
            '\nor send object cannot be updated.',
      13211: 'CAN warning state.'
            '\nAn unusual amount of errors occurred on the CAN bus.',
      13212: 'CAN bus off.'
            '\nToo many errors occurred on the CAN bus.'
            '\nNo more CAN messages can be sent or received.'
            '\nIf IOTCL_INACAN_SETPAR was called with restart_at_busoff = 1,'
            '\nthe driver tries to exit this state automatically by resetting'
            '\nthe CAN controller.'
            '\nIf restart_at_busoff was set to 0, this state can only'
            '\nbe exited by re-initializing the controller with IOCTL_INACAN_SETPAR.',
      13213: 'Error during CAN initialization.'
            '\nThe CAN controller cannot be initialized,'
            '\ne.g. due to an incorrect I/O port address for IOCTL_INACAN_SETPAR.',
      13214: 'Error during CAN start.'
            '\nThe CAN controller cannot be started,'
            '\ne.g. due to an incorrect I/O port address for IOCTL_INACAN_SETPAR.',
      13215: 'Error during CAN reset.'
            '\nThe CAN controller cannot be reset,'
            '\ne.g. due to an incorrect I/O port address for IOCTL_INACAN_SETPAR.',
      13216: 'Error during configuration.'
            '\nInternal driver error: The receive or send object cannot be configured,'
            '\nfor example due to an incorrect object number.',
      13217: 'Error during FIFO initialization.'
            '\nThe receive FIFO cannot be initialized,'
            '\ne.g. because the necessary memory cannot be requested.'
            '\nThis error is only delivered with driver version 1.30 or lower.',
      13218: 'Failed to start timeout.'
            '\nWindows system error: A timeout cannot be started.',
      13219: 'Failed to create semaphore.'
            '\nWindows system error: A semaphore for waiting in synchronous mode'
            '\ncannot be created.',
      13220: 'Insufficient memory available.'
            '\nWindows system error: Required memory could not be requested'
            '\nfrom the system.',
      13221: 'Impermissible handle.'
            '\nInternal driver error: Data structures required for this request'
            '\ncould not be found.',
      13222: 'Invalid CAN ID.'
            '\nAn invalid CAN message ID was specified at IOCTL_INACAN_WRITE'
            '\nor read by the CAN controller.',
      13223: 'Invalid CAN data length.'
            '\nAn invalid CAN message data length (>8) was specified'
            '\nwith IOCTL_INACAN_WRITE or read by the CAN controller.',
      13224: 'Error locking memory.'
            '\nWindows system error: Memory areas used in asynchronous mode'
            '\ncould not be locked,'
            '\ne.g. due to an invalid address for <OutBuf> or <InBuf>'
            '\nor structure OVERLAPPED for IOCTL_INACAN_READ or IOCTL_INACAN_WRITE.',
      13225: 'CAN not ready.'
            '\nThe CAN controller has not yet been started with IOCTL_INACAN_SETPAR.',
      13226: 'Device error.'
            '\nOnly with INACAN_LS172_PCI/ISA: An error response was received'
            '\nwhen communicating with an LS172 card.'
            '\nCause can be e.g. incompatibility of driver and LS172 firmware'
            '\nor an error in the driver.',
      13227: 'IRQ overflow.'
            '\nToo many IRQs. The PC may be too slow or too loaded down to process'
            '\nthe CAN messages occurring on the CAN bus.',        
      13228: 'Protocol error.'
            '\nAn unknown and invalid response was received from the LS172 card.',
      13229: 'No RTR object created/available'
            '\nEither no RTR object was created with IOCTL_INACAN_RTR_DEFINE'
            '\nor there are too many RTR objects active at the same time.'
            '\nThe maximum number of RTR objects that can be active at'
            '\nthe same time depends on the device.',
      13230: 'Error requesting data for RTR object',
      13231: 'Error updating data for RTR object',
      13232: 'Incorrect LS172 firmware version.'
            '\nThis error occurs in the following cases:'
            '\n1. With IOCT_INACAN_UPDATE if the firmware version is lower'
            '\n   than 1.90 (LS172.4) or lower than 2.40 (LS172.6x).'
            '\n2. With IOCTL_INACAN_WRITE and IOCTL_INACAN_REQUEST when sending'
            '\n   extended IDs >25 bits if the firmware version is lower than 2.00 (LS172.4) '
            '\n   or lower than 2.80 (LS172.6x).'
            '\n3. With IOCTL_INACAN_SETPAR if the baud rate INACAN_BAUD_800K'
            '\n   is to be set and the firmware version is lower than 2.10 (LS172.4)'
            '\n   or lower than 2.90 (LS172.6x).',
      13233: 'LS172 device busy.'
            '\nThis error occurs when a command cannot be written to the LS172'
            '\nbecause the send FIFO of the LS172 is full.',
      13234: 'RTR object already in use.'
            '\nThe RTR object with the specified ID has already been specified'
            '\nfor another path opened with CreateFile'
            '\nwith IOCTL_INACAN_RTR_DEFINE (is being used by another application).',
      13235: 'Error registering RTR object',
      13236: 'Error unregistering an RTR object',
      14300: 'The specified module type (MT=...) is unknown.'
            '\nThe specified module type (MT=...) is unknown.'
            '\nTherefore, no BR module can be generated.',
      14301: 'The specified BR module type (MT=...) is unknown.'
            '\nThe specified BR module type (MT=...) is unknown.'
            '\nTherefore, no BR data object can be created. Valid type: BRM',
      14302: 'The specified NC data object type (MT=NC_...) is unknown.'
            '\nThe specified NC data object type (MT=NC_...) is unknown.'
            '\nTherefore, no NC data object can be generated.'
            '\nValid types: NC_CNC, NC_ZPO, NC_TDT, NC_RPT, NC_CAM and NC_CAP',
      14303: 'The specified data is invalid.'
            '\nThe specified data is invalid.'
            '\nIt could be that the file does not contain any data'
            '\nor cannot be opened for reading.',
      14304: 'Information required to generate the BR module is invalid or missing.'
            '\nThe following information is required to create a BR module:'
            '\nModule type (MT=....), module info (MI=....), module name (MN=...),'
            '\nversion number (MV=...), section length (SL=...),'
            '\nsection index (SI=...), section data (must be loaded from a file).'
            '\nOne of the pieces of information needed to generate'
            '\nthe BR module is not defined.',
      14305: 'The module type has not been specified.'
            '\nThe module type has not been specified or is invalid (MT=).',
      14306: 'The module info has not been specified.'
            '\nThe module info has not been specified or is invalid (MI=).',
      14307: 'The module name has not been specified.'
            '\nThe module name has not been specified or is invalid (MN=).',
      14308: 'The version number has not been specified or is incorrect.'
            '\nThe version number has not been specified or is invalid (MV=).'
            '\nCan happen if the version number is unknown'
            '\nor not possible (e.g. with ChangeVer() call to determine own version).',
      14309: 'The specified section is invalid.'
            '\nThe length and data of the desired section in the BR module are invalid'
            '\n(e.g. length equals 0).'
            '\nIt is possible that the file does not contain any data'
            '\nor that the file cannot be opened for reading.',
      14310: 'The index of the section has not been specified.'
            '\nThe index of the section has not been specified or is invalid (SI=).'
            '\nIt is possible that the section with this index does not exist.',
      14311: 'The special module type is unknown.'
            '\nThe special module type is unknown, '
            '\ni.e. this BR module is not a valid NC data object.'
            '\nReverse translation using brncmgen.dll is therefore not possible.'
            '\nAll NC data objects must have a valid special module type.'
            '\nThe string is not permitted to contain MT=NC_.',
      14312: 'The specified module is not an NC data object.'
            '\nThe specified module is not an NC data object'
            '\nbecause the module type is not equal to (hex)46/(dec)70'
            '\nand therefore cannot be reverse translated.',
      14313: 'The module does not contain any data for reverse translation.'
            '\nThe specified BR module does not contain any data for reverse translation'
            '\n(the length of the data in the section is 0).',
      14314: 'The specified module is not a BR data object.'
            '\nThe specified module is not a BR module'
            '\nbecause the module type is not equal to (hex)41/(dec)65'
            '\nand therefore cannot be reverse translated.',
      14315: 'The language cannot be found.'
            '\nThe specified language is invalid for reverse translation.'
            '\nReverse translation is only supported for German (RL=DEU)'
            '\nor English (RL=ENG). No comments are generated.',
      14316: 'An error occurred while reading the data.'
            '\nAn error occurred while reading the data from the section.'
            '\nThe data may be incomplete, or the BR module or file may contain errors.',
      14317: 'Error evaluating text data.'
            '\nError evaluating text data.'
            '\nIt is possible that not enough numbers have been entered.'
            '\nThis is the case, for example, if 3 is specified'
            '\nas the number in a zero point offset table,'
            '\nbut 3 x 3 axis offsets are not specified.'
            '\nIt may also be due to a syntax error in the text.'
            '\nIt is not considered an error if 4 x 3 axis offsets are specified,'
            '\nbut only 3 offset sets are specified as the number.',
      14318: 'The structure for the desired data type is not defined (NCT=...).'
            '\nThe structure for the desired data type is not defined (NCT=...).'
            '\nThere is no structure in the NC database for the desired data type'
            '\n(NCHWID=... and MV=... must also be taken into account).',
      14319: 'BuildModule() or RebuildModule() is not permitted to be called'
            '\nduring PVI download or upload.'
            '\nFor InitParameterModules, data must be read from the NC database,'
            '\nwhich is not possible at this time.'
            '\nFunction AscToBr() should be used to create BR modules.'
            '\nFunction BrToAsc() should be used to create ASCII modules.',
      14320: 'Internal error:data from the section could not be written'
	  		'\nThe data from the section could not be written to the BR module.',
      14321: 'Internal error:file management error'
	  		'\nVM file management error the data could not be written.',
      14322: 'Internal error:more sections could be created'
	  		'\nNo more sections could be created in the BR module.',
      14323: 'Internal error:BR module could not be completed'
	  		'\nThe BR module could not be completed in memory.',
      14324: 'Internal error:memory could not be requested'
	  		'\nVM file management error, memory could not be requested.',
      14325: 'Internal error:Data could not be transferred'
	  		'\nData could not be transferred from the VM memory to the BR module.',
      14326: 'No memory could be requested and reserved.'
             '\nThere is no more free memory in the system (exit and restart Windows,'
             '\ndelete files, check page file, exit programs, etc.).',
      14327: 'Internal error: Not enough storage space was reserved for the data'
             '\n(calculation error).',
      14328: 'Internal error: Non-released memory  there could be gaps in memory.'
            '\nA pointer used to allocate memory is not NULL.'
            '\nThe memory to which the pointer points cannot be freed'
            '\nbecause it has not been allocated by this DLL.'
            '\nA program crash could be caused when the memory is freed'
            '\nbecause the DLL has no access rights to the memory.',
      14780: 'Fatal error. Internal error of the SNMP line',
      14781: 'Illegal object hierarchy.'
            '\nThe specified process object type (e.g. Line, Device, Station, Pvar)'
            '\nis not compatible with that of the higher-level process object.'
            '\nFor example, an attempt was made to set up a device process object'
            '\nunder a station process object.',
      14782: 'Illegal or unknown object name.\nThe name of the line object is illegal.'
            '\nThe device name (if specified) is not SNMP, the MAC address is illegal,'
            '\nor the variable name is unknown'
            '\n(does not correspond to any variables supported by the SNMP line).'
            '\nThe name of the line object is determined by the connection name'
            '\n(PVI parameter CD).',
      14783: 'Error initializing SNMP library (BrSnmp.dll).',
      14784: 'SNMP library protocol error (BrSnmp.dll)',
      14785: 'No data received (timeout).'
            '\nWhen accessing SNMP variable data, no response was received'
            '\nwithin the specified timeout time.',
      14786: 'Write access to SNMP variable data denied',
      14787: 'Invalid SNMP variable data received',
      14800: 'Fatal error in MODBUS DLL',
      14801: 'Function not supported by MODBUS hardware',
      14802: 'MODBUS hardware denies access to specified address',
      14803: 'Value for address in MODBUS function not permitted',
      14804: 'MODBUS device error'
            '\nAn error has occurred in the MODBUS device.'
            '\nThe communication watchdog was triggered.',
      14806: 'MODBUS device damaged.'
            '\nUsually occurs when a module is plugged in during operation'
            '\nand can usually be corrected by reattempting read or write access.',
      14808: 'Faulty connection to MODBUS controller.'
            '\nA connection to the MODBUS controller could not be established.'
            '\nThe error reported by Windows can be read from the log file'
            '\nof the line (see PVI data logger).',
      14809: 'Request could not be processed because there is no connection'
            '\nto the MODBUS hardware.',
      14810: 'Impermissible MODBUS client number.'
            '\nNo client object was created for the specified ID.',
      14811: 'Response with incorrect transaction number received',
      14812: 'Impermissible MODBUS device ID',
      14813: 'MODBUS response data contains errors.'
            '\nThe received response data is not permitted for the sent request.'
            '\nSpecific information about the incorrect response'
            '\ncan be obtained from the log file of the line">.',
      14814: 'Error initializing Winsock library.'
            '\nThis error also occurs if the installed Windows Sockets version'
            '\nis not supported. V2.02 or higher is required.'
            '\nThe error reported by Windows can be read from the log file of the line',
      14816: 'Error registering or instantiating MODBUS response handler.'
             '\nThe error reported by Windows can be read from the log file of the line.',
      14818: 'Transaction could not be executed due to timeout or network error.'
             '\nSpecific information about the cause of the error can be read'
             '\nfrom the log file of the line.',
      14819: 'Error sending request to MODBUS device.'
              '\nCaused by a problem in the network subsystem.'
              '\nThe exact cause can be read from the log file of the line.',
      14820: 'Error receiving response from MODBUS device.'
              '\nCaused by a problem in the network subsystem.'
              '\nThe exact cause can be read from the log file of the line.',
      14822: 'Error in the configuration file.'
              '\nThis error also occurs if the version of the configuration file'
              '\nis not supported.'
              '\nSpecific information about the error can be read from the'
              '\nlog file of the line.',
      14825: 'Internal error in MODBUS line DLL',
      14826: 'Illegal object name.'
              '\nThe name of a process object is not allowed.'
              '\nIt is possible that a variable name is neither a defined process variable'
              '\nor a valid address value.',
      14827: 'Device not supported',
      14828: 'Impermissible address for MODBUS array variable',
      14829: 'Impermissible data type for MODBUS array variable',
      14830: 'Impermissible number of elements in MODBUS array variable',
      14831: 'Impermissible index for MODBUS array variable',
      14832: 'Error transferring configuration to station.'
              '\nThis error also occurs if a station object detects a mismatching'
              '\nconfiguration during setup,'
              '\nbut the MODBUS controller is already connected to other clients.'
              '\nOnly the first client can perform a transfer,'
              '\nas this would lead to unpredictable behavior for clients already connected.',
      14840: 'Fatal error. Internal error of the ADI line',
      14841: 'Illegal object hierarchy.'
              '\nThe specified process object type (e.g. Line, Device, Task, Pvar)'
              '\nis not compatible with that of the higher-level process object.'
              '\nFor example, an attempt was made to set up a device process object'
              '\nunder a task process object.',
      14842: 'Illegal object name.'
              '\nThe name of the line object is illegal.'
              '\nThe device name (if specified) is not PC or PANEL or the variable name'
              '\nis unknown (does not correspond to any variables supported by the ADI line).'
              '\nThe name of the line object is determined by the connection name'
              '\n(PVI parameter CD).',
      14843: 'Impermissible parameter (CD).'
              '\nThe connection description (PVI parameter CD)'
              '\ncontains an invalid impermissible parameter.',
      14844: 'Windows system error when setting up system resource.'
              '\nAn attempt to set up a system resource was denied by Windows with an error.',
      14845: 'Device cannot be opened.'
              '\nThe ADI driver is either not installed correctly or not running'
              '\n(the status of the ADI driver can be checked in the Windows Device Manager).',
      14846: 'Device error.'
              '\nThe device addressed via ADI returned an error, e.g. Busy or Not Ready.',
      14847: 'Illegal object data.'
              '\nWhen writing to a variable process object, invalid data was specified,'
              '\ne.g. the value 4 was written to the variable Leds[0]'
              '\n(the valid range is 0 to 3).',
      14848: 'Incorrect version / version conflict.'
              '\nA version conflict has occurred, e.g. a firmware version'
              '\ndoes not match the hardware revision.',
      14849: 'Function not implemented.'
              '\nThe variable process object cannot be used because the required function'
              '\nis not built into the ADI.',
      14850: 'Function not supported.'
              '\nThe variable process object cannot be used because the required'
              '\nfunction is not supported by the ADI'
              '\n(e.g. because the installed BIOS version is too old).',
      14851: 'No data available from device.'
              '\nNo data can be read from the device for the variable process object.',
      14852: 'Access error.'
              '\nThe variable process object cannot be used because'
              '\nthe necessary data cannot be accessed  for example,'
              '\nbecause it is blocked by other access.',
      14853: 'Device not connected.'
              '\nThe variable process object cannot be used because the addressed device'
              '\n(e.g. an Automation Panel) is not connected.',
      14854: 'Device is no longer available.'
              '\nThe variable process object cannot be used'
              '\nbecause the addressed device no longer exists'
              '\n(e.g. an Automation Panel has been unplugged).',
      14855: 'Timeout for device access.',
      14870: 'Illegal object hierarchy.'
              '\nThe specified process object type (e.g. Line, Device, Task, Pvar)'
              '\nis not compatible with that of the higher-level process object.'
              '\nFor example, an attempt was made to set up a device process'
              '\nobject under a task process object.',
      14871: 'MTC protocol error.'
              '\nAn error has occurred during communication with MTC'
              '\n(e.g. timeout or incorrect checksum).',
      14872: 'Fatal error. Internal error of MTC line',
      14873: 'Illegal object name.'
              '\nThe name of the line object is illegal.'
              '\nThe device name (if specified) is not MTC or the variable name is unknown'
              '\n(does not correspond to any variables supported by the MTC line).'
              '\nThe name of the line object is determined by the connection name'
              '\n(PVI parameter CD).',
      14874: 'No key switch defined.'
              '\nVariables MkeySwitches and MkeySwitchesOffset cannot be used'
              '\nbecause no key switch is defined.'
              '\nA key switch can be defined with B&amp;R MKEY Utilities.',
      14875: 'Illegal object data.'
              '\nWhen writing to a variable process object, invalid data was specified,'
              '\ne.g. the value 4 was written to variable MkeyLeds[0]'
              '\n(the valid range is 0 to 3).',
      14876: 'MTC device cannot be opened.'
              '\nAn error occurred when opening the MTC device.'
              '\nB&R MTC Utilities may not yet be installed.',
      14877: 'Incorrect MTC version.'
              '\nThe variable process object cannot be used because the required'
              '\nMTC version is not installed. Variables UserLed, MkeyLedMatrix,'
              '\nKeySwitches, KeySwitchesOffset, WatchdogTime and Watchdog'
              '\nrequire MTC Version 00.10 or higher.',
      14878: 'No display connected.\nThe variable process object cannot be used'
              '\nbecause no display is connected.'
              '\nThis applies to variables FpdOperatingHours, FpdPowerOnCycles,'
              '\nFpdOverTempHours, FpdTemperature, FpdContrast, FpdBrightness,'
              '\nFpdDefaultContrast, FpdDefaultBrightness and FpdMkeyLedRegisters.',
      14879: 'Scan codes not defined.\nThe variable process object cannot be used'
              '\nbecause no key scan codes are defined.'
              '\nScan codes can be defined using B&R MKEY Utilities.'
              '\nThis applies to variables Mkeys and MkeyMatrix.',
      14880: 'Impermissible parameter (CD).'
              '\nThe connection description (PVI parameter CD) contains an'
              '\ninvalid impermissible parameter.',
      14881: 'Windows system (9x/NT) not recognized.'
              '\nThe MTC device cannot detect whether the system used'
              '\nis Windows 9x or Windows NT.',
      14940: 'Error initializing MiniNet DLL',
      14941: 'Device object already exists (only one device object permitted)',
      14942: 'Illegal object hierarchy',
      14943: 'No connection to PLC or MiniNet protocol error',
      14944: 'Fatal error in MiniNet line',
      14945: 'Max. protocol length exceeded',
      14946: 'Illegal object name',
      14960: 'Reset performed',
      14961: 'Index error',
      14962: 'Index/Command contradiction',
      14963: 'Unknown command',
      14964: 'Command already executed',
      14965: 'Invalid parameter',
      14966: 'Index reset',        
      14970: 'Fatal error',
      14973: 'Windows system error when setting up system resource.'
              '\nAn attempt to set up a system resource was denied by Windows with an error.',
      14979: 'Illegal CAN ID (in connection description)',
      14980: 'Illegal object hierarchy',
      14982: 'Read and write attributes are set',
      14986: 'Write timeout',        
      14988: 'Illegal IF parameter (connection description of device object)',        
      15000: 'Basis for PviServices error and status numbers',        
      15001: 'Read and write access not permitted'
              '\nThis error is returned if an access method is called for an object'
              '\nand the object is not yet or no longer initialized.',
      15002: 'Multiple method calls not permitted.'
              '\nSome methods do not have a queue, so it is necessary to wait'
              '\nfor the response before calling them again.',
      15003: 'Method call without function'
              '\nFor example, if ChangeConnection is called without'
              '\nchanging the interface parameters,'
              '\nthis has no effect and therefore this method is not executed at all.'
              '\n(In this case, no event is triggered!)',        
      27300: 'Tag not specified in configuration file.'
              '\nThe tag name specified for function WriteTag or ReadTag does not exist'
              '\nin the configuration file of the PviConfigurator.',
      27301: 'Invalid data type for write access.'
              '\nThe WriteTag does not support write access to string arrays,'
              '\nstructures and data.',
      27302: 'Invalid data type for read access.'
              '\nReadTag does not support read access to string arrays, structures or data.',
      27303: 'Access to string arrays not supported.'
              '\nReadTag and WriteTag do not support data with string array type VARIANT.',
      27304: 'Writing and reading of VARIANT data type not supported.'
              '\nThe ReadTag and WriteTag functions do not support the initialized VARIANT type.',
      27305: 'Reading and writing multi-dimensional arrays is not supported.'
              '\nReadTag and WriteTag functions do not support multidimensional'
			  '\narrays of type VARIANT.',
      27306: 'Writing and reading arrays with more than 65535 elements is not supported.'
              '\nReadTag and WriteTag functions do not support arrays with'
              '\nmore than 65535 elements in type VARIANT.',
      27307: 'Logical path of SetConnection and GetConnection functions does not exist.'
              '\nImportant! Spaces at the beginning and end of the character string are applied.',
      27308: 'Function SetConnection or GetConnection function was called'
              '\nbefore PviControl was initialized.',
      27309: 'The resource name of function ReadResource function does not exist.'
              '\nImportant! Spaces at the beginning and end of the character string are applied.',
      27310: 'Invalid offset in resource name.'
              '\nThe offset in argument Resource name of function ReadResource is invalid.'
              '\nThe offset contains invalid characters.',
      27311: 'Invalid resource name declaration.'
              '\nThe declaration of argument Resource name of function ReadResource is invalid.'
              '\nSpecified offset was not between [ and ].',
      27312: 'Invalid offset of resource name.'
              '\nThe offset in argument Resource name of function ReadResource is invalid.'
              '\nThe offset is greater than the length of the resource array.',
      27313: 'Argument TagData of function ReadBuffer or WriteBuffer is invalid.'
              '\nVARIANT was pre-initialized with an invalid format.'
              '\nOnly bytes can be processed.',
      27314: 'Writing & reading the buffer of multidimensional arrays not supported.'
              '\nFunctions WriteBuffer and ReadBuffer do not support'
              '\nmultidimensional arrays of type VARIANT.',
      27315: 'Writing and reading arrays with more than 65535 elements is not supported.'
              '\nFunctions WriteBuffer and ReadBuffer do not support arrays with'
              '\nmore than 65535 elements in type VARIANT.',
      27316: 'Tag not specified in configuration file.'
              '\nThe tag name specified for function WriteBuffer or ReadBuffer does not exist'
              '\nin the configuration file of the PviConfigurator.',        
      27350: 'Alarm server restart.'
              '\nThe AlarmServer has been reinitialized and is rereading the alarm configuration.',
      27351: 'Object does not exist.'
              '\nThe requested alarm object does not exist.Causes: name misspelled,'
              '\nincorrect configuration or alarm object does not exist',
      27352: 'Invalid format of alarm condition.'
              '\nThe condition (LowLow, Low, High or HighHigh) has an invalid format'
              '\nor does not exist.'
              '\nCauses: name misspelled, incorrect configuration or alarm object does not exist;'
              '\nthe specified fixed value is not a valid number.',
      27353: 'Configuration file missing.'
              '\nThe name of a configuration file was not specified'
              '\nor an incorrect filename was specified.',
      27354: 'Alarm reference not found.'
              '\nThe specified reference name cannot be found'
              '\nbecause it does not exist or was misspelled.'
              '\nThe configuration may have been changed.',
      27355: 'Bridging not possible.'
              '\nThe specified alarm cannot be bridged because it is not based'
              '\non an alarm definition.'
              '\nThe alarm usually results from PVI errors, which are specially marked as such.'
              '\nHowever, it can also be a follow-up error of error 27354.',        
      27356: 'No language change.'
              '\nThe selected language is already active,'
              '\nso switching is not necessary and will not be performed.',
      27357: 'Unknown language.'
              '\nThis language column does not exist or the name was not spelled correctly;'
              '\nlanguage names are CASE sensitive!',
      27358: 'No neutral language.'
              '\nLanguage column Neutral does not exist.'
              '\nThis column must always be present!'
              '\nNormally it is not possible to remove this column.'
              '\n(Only possible if resource file is manipulated manually!)',
      27359: 'Link object does not exist.'
              '\nAn attempt was made to process an alarm (bridge)'
              '\nwhose alarm variable does not yet have a link object.'
              '\nThis is a follow-up error of a PVI system error.',
      27360: 'No alarm events recorded.'
              '\nAttempted to save the alarm history, but no alarm events have been recorded yet.',
      27361: 'Invalid history file.'
              '\nThe file is not an alarm history file or the format could not be recognized.'
              '\nThis can only be due to manual manipulation of the file.',
      27362: 'PVI system alarms cannot be acknowledged.'
              '\nIt is not possible to acknowledge an alarm with this status,'
              '\nas it is a PVI system error'
              '\n(e.g. PLC connection interrupted).'
              '\nIn this case, the confirmation variable is also usually not available.'
              '\nIf such alarms are not to be entered, the alarm must be bridged.',
      27363: 'Multiple bypass not possible.'
              '\nIf an attempt is made to bypass an alarm that has already been bypassed,'
              '\nthis is denied by the alarm system.'
              '\nAlarms that have already been bypassed cannot be bypassed again!',
      27364: 'Not possible to remove multiple bypasses.'
              '\nThe alarm is not bypassed and therefore cannot be un-bypassed.'
              '\nIf an attempt is made to remove the bypass of an alarm that has'
              '\nnot been bypassed, this request will be denied by the alarm system.'                                                             
    }


    def __init__(self, error):
        message = self._messages.get(error, "")        
        super().__init__( f"\n\nPvi-Error {error} : {message}" )

if __name__ == '__main__':
	# report too long hint textes
	for key, val in PviError._messages.items():
		lengths = [len(t) for t in val.split('\n')]
		maxlength = max(lengths)
		if maxlength > 80:
			print(f'PviError._messages[{key}]: text too long ! (Rows:{lengths}')



# [Profiler](https://help.br-automation.com/#/en/4/diagnostics_support%2Fdiagnosis%2Fprofile%2Fdiagnosis_profile.html)

The Profiler can be used to measure and display important system data such as task runtimes, system and stack loads, etc. This can be necessary to determine how much idle time remains in a task class or which task generates a sporadic increased demand for time.

The profiler can also record and analyze events determined by the user (user events) such as interrupt service routine and library function time demands, as well as time differences between events.

## [Recording profiler data](https://help.br-automation.com/#/en/4/diagnostics_support%2Fdiagnosis%2Fprofile%2Frecord%2Fdiagnosis_profile_record.html)

To record profiler data, the configuration data has to be installed first before the profiler can be started. After the profiler stops and measurement ends, profiler-specific data should be erased on the target system so that memory is not used unnecessarily.

## Reading profiler data

In fact there is no real support in PviCom.dll for extracting the contents in a profiler module but this topic fits very well into the PVI category.
Handling profiler files is still beta since the file format is not public, the known structure was found out by reverse engineering.

## Examples

find the following examples on GitHub [github.com/hilch/Pvi.py](https://github.com/hilch/Pvi.py/tree/main/examples)

### [profiler1.py](https://github.com/hilch/Pvi.py/tree/main/examples/profiler1.py)

extract all profiler data *.pd file and save it to csv

### [profiler2.py](https://github.com/hilch/Pvi.py/tree/main/examples/profiler2.py)

extract all profiler data from a systemdump container and save it to csv